from unittest import TestCase
from src.app import create_app
from src.core.database import database
from src.core.config import config


class IntegrationBaseTest(TestCase):
    jwk = {
        'use': 'sig',
        'kty': 'RSA',
        'kid': '99ce63c2-b47a-4b40-ae53-ac02940e8e53',
        'alg': 'RS256',
        'n': 'wOPf2xfG6dpYkCmj9ZzSmoYBIeHQTskTf_z0Mv6gOKJPdfF3RQns0ZJuvJzfYPtS5QQtz1LDnA7V6h7WP9HV2bHcR1C1dCG8etIpmpNj3QqfjN09or4FyecXhhwThbd77aNm56lAW7bmwGLkEd-sX5SzlitLvQSDLFFQo4EAx44WuT4Jl6dLTiT4HYR-jVBRTzSBju1HDjaYEHjRgRDLnzLzsKp0AA4cJ3NzIcyWSZgWNpLp3iFvFudMA4L1EfzWujCRo8QkFv3lwCsk6qjuHEDPlulp-LgcACDurYm1lhiyOgLt9HgTBDvyNEHgoP6yheJD3Ljl66rylQJlJfE_Sw',
        'e': 'AQAB'
    }
    token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6Ijk5Y2U2M2MyLWI0N2EtNGI0MC1hZTUzLWFjMDI5NDBlOGU1MyIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsidnVlIl0sImV4cCI6MTYxNDU2NjAyOCwiaWF0IjoxNTgzMDMwMDI4LCJpc3MiOiJodHRwOi8vMTI3LjAuMC4xOjQ0NTUvIiwianRpIjoiMDY3OTIxYzgtNmM1Mi00OTViLWFmYTYtYWRjYjg5YjAyMWYwIiwibmJmIjoxNTgzMDMwMDI4LCJzdWIiOiI4NTRjOWE5Yi00YTRhLTQxMGYtODY3Yy05OTg1YzE3ODc4ZDgifQ.NFJvBSfQEhJolpQ1Tcaxs3kKopXft0DTYSqhA4kmKWHjAEdPBLMS_dO5RUPxY-BXOctpmQ4FcOPGYOGvK-r1g30m92NN48iW4aaPCY-a0M6P6pVlrIRlM2dNgRHpK_cqWTqNyKaGYDd1sfj8SQ43cxoG8kEdFPdmoC86FNAd39YeQNYUqGExowt14wVNC6l1a-FZcLoFP3HDYelZwdfmTJxHIo33V5WQE-peAWIIJL2sDsonbbMVJkpepgchFd0BkmtmvQyKgx5CfUdKz6HaKpCMM7JLzlBTGHHrIusyD_-eC3IR5s2Kx6OwNqhBnyGWQNVn0PGIv-IYciQrrHXjew'
    token_subject = '854c9a9b-4a4a-410f-867c-9985c17878d8'

    def setUp(self):
        database.disconnect()
        app = create_app(config['testing'])

        self.app = app.test_client()
        self.app_context = app.app_context()
        self.database = database.get_db()

    def tearDown(self):
        for collection in self.database.list_collection_names():
            self.database.drop_collection(collection)
