import json
import xmltodict
import requests
from .utils import getDistrictIdByAbacusId
from .utils import getRegionIdByAbacusId

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from common.utils import check_permission


from scoring.models.crif import CRIF
from scoring.models.scoring_type import ScoringType
from scoring.models.scoring_type.model import UID_CRIF_CREDIT
from oxus.settings import CRIF_URL, CRIF_LOGIN, CRIF_PASSWORD
from request_credit.models.r_credit import RequestCredit

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crif_swift_check(request):
        check_permission(request.user, CRIF, 'can-crif-get-information-swift_crif')

        data = json.loads(request.body.decode('utf-8')) if request.body else {}
        swift_id = data.get('swiftId', None)
        credit = RequestCredit.objects.get(id=swift_id)

        gender = 'M' if credit.customer.gender == 'male' else 'F'
        name = credit.customer.name.split()
        birthday = credit.customer.birthday.strftime('%d%m%Y')
        passport = credit.customer.passport.replace('A', 'А').replace('_', '') # change latin 'A' to cyrillic 'А' and remove unused symbol
        district = credit.customer.address.town.name
        district_id = credit.customer.address.town.abacus_id
        region_id = credit.customer.address.town.region.abacus_id
        created = credit.created.strftime('%d%m%Y')
        installment = credit.approve_installment or credit.request_installment
        amount = credit.approve_amount or credit.request_amount
        product = 11 if credit.credit_product.id == 2 else 10

        clint_data = f"""
        <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:crif-message:2006-08-23" xmlns:urn1="urn:crif-messagegateway:2006-08-23">
            <soap:Header>
                <urn:Message GId="" MId="" MTs="2018-07-04T15:36:56">
                    <!--Optional:-->
                    <urn:C UD="?" UId="{CRIF_LOGIN}" UPwd="{CRIF_PASSWORD}">
                        <!--You may enter ANY elements at this point-->
                    </urn:C>
                    <!--Zero or more repetitions:-->
                    <urn:P SId="CB" PId="RI_Req" PNs="urn:RI_Req.2012-04-27.000">
                        <!--You may enter ANY elements at this point-->
                    </urn:P>
                    <!--Optional:-->
                    <urn:Tx TxNs="urn:crif-messagegateway:2006-08-23">
                        <!--You may enter ANY elements at this point-->
                    </urn:Tx>
                    <!--You may enter ANY elements at this point-->
                </urn:Message>
            </soap:Header>
            <soap:Body>
                <urn1:MGRequest>
                    <![CDATA[
                    <RI_Req_Input>
                            <Subject>
                                <FISubjectCode></FISubjectCode>
                                <Individual>
                                    <Gender>{gender}</Gender>
                                    <FirstName>{name[1]}</FirstName>
                                    <Patronymic>{name[2] if len(name) > 2 else ''}</Patronymic>
                                    <Surname>{name[0]}</Surname>
                                    <PrevFirstName></PrevFirstName>
                                    <PrevSurname></PrevSurname>
                                    <MotherMaidenName></MotherMaidenName>
                                    <DateOfBirth>{birthday}</DateOfBirth>
                                    <PlaceOfBirth></PlaceOfBirth>
                                    <CountryOfBirth>TJ</CountryOfBirth>
                                    <INN>{credit.customer.INN}</INN>
                                    <Documents>
                                        <Main>
                                            <DocType>1</DocType>
                                            <DocSeriesAndNumber>{passport}</DocSeriesAndNumber>
                                            <DocIssueDate></DocIssueDate>
                                            <DocIssueAuthPlace></DocIssueAuthPlace>
                                        </Main>
                                    </Documents>
                                    <Address>
                                        <Main>
                                            <StreetNumAndName>{credit.customer.address_street}</StreetNumAndName>
                                            <City>{district}</City>
                                            <District>{getDistrictIdByAbacusId(district_id)}</District>
                                            <Region>{getRegionIdByAbacusId(region_id)}</Region>
                                            <PostCode></PostCode>
                                            <Country>TJ</Country>
                                            <LivedSinceDate></LivedSinceDate>
                                        </Main>
                                    </Address>
                                    <Contact>
                                        <ContactType></ContactType>
                                        <ContactNumber></ContactNumber>
                                    </Contact>
                                    <SoleTrade>
                                        <SoleTradeName></SoleTradeName>
                                        <RegistrationNum></RegistrationNum>
                                        <EstablishDate></EstablishDate>
                                        <RegistrationPlace></RegistrationPlace>
                                        <ContactNumber></ContactNumber>
                                    </SoleTrade>
                                    <Employement>
                                        <EmployerName></EmployerName>
                                        <Status></Status>
                                        <ContactNumber></ContactNumber>
                                        <DateHired></DateHired>
                                        <DateTermination></DateTermination>
                                        <OccupationType></OccupationType>
                                        <JobTitle></JobTitle>
                                        <AnnualIncome></AnnualIncome>
                                    </Employement>
                                </Individual>
                            </Subject>
                            <Link>
                                <Role>A</Role>
                            </Link>
                            <Contract>
                                <FIContractCode></FIContractCode>
                                <ReqDate>{created}</ReqDate>
                                <ContractType>{product}</ContractType>
                                <Currency>TJS</Currency>
                                <Instalment>
                                    <InstallmentNum>{installment}</InstallmentNum>
                                    <InstallmentAmn></InstallmentAmn>
                                    <Amount>{amount}</Amount>
                                    <Periodicity>M</Periodicity>
                                </Instalment>
                            </Contract>
                        <Report>
                        <Type>1</Type>
                        </Report>
                        </RI_Req_Input>
                    ]]>
                </urn1:MGRequest>
            </soap:Body>
        </soap:Envelope>"""

        req = requests.post(CRIF_URL, headers={'Content-Type': 'text/xml; charset=utf-8', 'Accept-Language': 'ru-RU', 'Content-Language': 'ru-RU'}, data=clint_data.encode('utf-8'))
        response = req.text
        response = response.replace('&gt;', '>')
        response = response.replace('&lt;', '<')

        dict_data = xmltodict.parse(response)
        dict_data = dict_data['soap:Envelope']['soap:Body']['MGResponse']['MGResponse']['RI_Req_Output']
        json_data = json.dumps(dict_data)

        CRIF.objects.create(
            request_credit_id=swift_id,
            type=ScoringType.objects.get(uid=UID_CRIF_CREDIT),
            data=json_data,
            generated_by=request.user,
        )
        # print(json_data)
        return JsonResponse({'message': 'created'} )
