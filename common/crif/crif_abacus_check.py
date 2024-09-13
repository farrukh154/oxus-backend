import json
import xmltodict
import requests
import pypyodbc as odbc
from common.abacus.connection import connection_string
from .utils import getDistrictIdByAbacusId
from .utils import getRegionIdByAbacusId
from django.core.exceptions import ValidationError

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from common.utils import check_permission


from scoring.models.crif import CRIF
from scoring.models.scoring_type import ScoringType
from scoring.models.scoring_type.model import UID_CRIF_CREDIT
from oxus.settings import CRIF_URL, CRIF_LOGIN, CRIF_PASSWORD

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crif_abacus_check(request):
        check_permission(request.user, CRIF, 'can-crif-get-information-abacus_crif')

        data = json.loads(request.body.decode('utf-8')) if request.body else {}
        abacus_client_id = data.get('abacusCustomerId', None)
        abacus_account_number = data.get('abacusAccountNumber', None)
        abacus_account_id = data.get('abacusCuAccountId', None)

        conn = odbc.connect(connection_string)
        cursor = conn.cursor()

        cursor.execute(f"""
            SELECT
                c.CustomerID,
                (CASE WHEN p.Gender=0 THEN 'M' ELSE 'F' END) Gender,
                SUBSTRING(p.Forename, CHARINDEX('|', p.Forename)+1, 100) FirstName,
                SUBSTRING(p.Forename, 1, CHARINDEX('|', p.Forename)-1) Surname,
                p.Surname Patronymic,
                REPLACE(CONVERT(CHAR(10), p.DateOfBirth, 103), '/', '') DateOfBirth,
                p.DrivingLicenceNumber as INN,
                REPLACE(REPLACE(p.SocialSecurityNumber, '_', ' '), 'A', N'А') DocSeriesAndNumber,
                ISNULL(adr.Address1, 'not set') StreetNumAndName,
                adr.County City,
                a.AccountNumber FIContractCode,
                CAST(l.ApplyAmountTotal * [dbo].OTJ_GetXR(cur.CurrencyID, 18, l.ApplyDate) AS integer) Amount,
                REPLACE(CONVERT(CHAR(10), l.ApplyDate, 103), '/', '') ReqDate,
                cur.Code Currency,
                lp.TermPeriodNum InstallmentNum,
				adr.StateID,
				adr.CountyID,
				(
					CASE
					WHEN AnalysisField.[Name]='Consumer Loan' OR AnalysisField.[Name]='Livelihood loan' OR AnalysisField.[Name]='Internal consumer loan' THEN '10'
					WHEN AnalysisField.[Name]='Business loan' THEN '12'
					ELSE '11' END
				) ContractType
            FROM CUAccount a
            INNER JOIN Customer c ON a.CustomerID = c.CustomerID
            LEFT JOIN CustomerPerson cp ON cp.CustomerID = c.CustomerID
            LEFT JOIN Person p on p.PersonID = cp.PersonID
            LEFT JOIN CustomerAddress ca ON c.CustomerID=ca.CustomerID and ca.AddressTypeID=1
            LEFT JOIN dbo.[Address] adr ON adr.AddressID=ca.AddressID
            LEFT JOIN CULoan l ON l.CULoanID=(SELECT TOP(1) l2.CULoanID FROM CULoan l2 WHERE
            l2.[Status]<>64 AND l2.CUAccountID=a.CUAccountID ORDER BY l2.ApplyDate DESC)
            LEFT JOIN CULoanPart lp ON lp.CULoanID=l.CULoanID
            LEFT JOIN CUProduct prod ON prod.ProductID=l.ProductID
            LEFT JOIN CUProductLoan pl ON pl.ProductID=prod.ProductID
            LEFT JOIN Currency cur ON cur.CurrencyID=prod.CurrencyID
			LEFT JOIN AnalysisLink ON AnalysisLink.ProductID=prod.ProductID and AnalysisLink.AnalysisFieldID between 7 and 15
			LEFT JOIN AnalysisField ON AnalysisField.AnalysisFieldID=AnalysisLink.AnalysisFieldID and AnalysisField.AnalysisGroupID=2
            WHERE a.CUAccountID = {abacus_account_id} AND a.ParentAccountID IS NULL
        """)
        columns = [column[0] for column in cursor.description]
        while True:
            row = cursor.fetchone()
            if not row:
                break
            result_dict = {column: row[column] for column in columns}

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
                                    <Gender>{result_dict['gender']}</Gender>
                                    <FirstName>{result_dict['firstname']}</FirstName>
                                    <Patronymic>{result_dict['patronymic']}</Patronymic>
                                    <Surname>{result_dict['surname']}</Surname>
                                    <PrevFirstName></PrevFirstName>
                                    <PrevSurname></PrevSurname>
                                    <MotherMaidenName></MotherMaidenName>
                                    <DateOfBirth>{result_dict['dateofbirth']}</DateOfBirth>
                                    <PlaceOfBirth></PlaceOfBirth>
                                    <CountryOfBirth>TJ</CountryOfBirth>
                                    <INN>{result_dict['inn']}</INN>
                                    <Documents>
                                        <Main>
                                            <DocType>1</DocType>
                                            <DocSeriesAndNumber>{result_dict['docseriesandnumber']}</DocSeriesAndNumber>
                                            <DocIssueDate></DocIssueDate>
                                            <DocIssueAuthPlace></DocIssueAuthPlace>
                                        </Main>
                                    </Documents>
                                    <Address>
                                        <Main>
                                            <StreetNumAndName>{result_dict['streetnumandname']}</StreetNumAndName>
                                            <City>{result_dict['city']}</City>
                                            <District>{getDistrictIdByAbacusId(result_dict['countyid'])}</District>
                                            <Region>{getRegionIdByAbacusId(result_dict['stateid'])}</Region>
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
                                <ReqDate>{result_dict['reqdate']}</ReqDate>
                                <ContractType>{result_dict['contracttype']}</ContractType>
                                <Currency>TJS</Currency>
                                <Instalment>
                                    <InstallmentNum>{result_dict['installmentnum']}</InstallmentNum>
                                    <InstallmentAmn></InstallmentAmn>
                                    <Amount>{result_dict['amount']}</Amount>
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

        # print(clint_data)
        req = requests.post(CRIF_URL, headers={'Content-Type': 'text/xml; charset=utf-8', 'Accept-Language': 'ru-RU', 'Content-Language': 'ru-RU'}, data=clint_data.encode('utf-8'))
        response = req.text
        response = response.replace('&gt;', '>')
        response = response.replace('&lt;', '<')
        # print(response)

        dict_data = xmltodict.parse(response)
        dict_data = dict_data['soap:Envelope']['soap:Body']['MGResponse']['MGResponse']['RI_Req_Output']
        # print(dict_data)
        if 'Error' in dict_data:
            raise ValidationError(f"{dict_data['Error']['Description']} {dict_data['Error']['Value']}")
        json_data = json.dumps(dict_data)

        CRIF.objects.create(
            abacus_customer_id=abacus_client_id,
            abacus_credit_id=abacus_account_id,
            abacus_account_number=abacus_account_number,
            type=ScoringType.objects.get(uid=UID_CRIF_CREDIT),
            data=json_data,
            generated_by=request.user,
        )
        # print(json_data)
        return JsonResponse({'message': 'created'} )
