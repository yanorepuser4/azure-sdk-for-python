from testcase import AppConfigTestCase
from devtools_testutils import recorded_by_proxy
from preparers import app_config_decorator_aad
import dns.resolver


class TestDnsPython(AppConfigTestCase):
    @recorded_by_proxy
    @app_config_decorator_aad
    def test(self, appconfiguration_endpoint_string):
        uri = appconfiguration_endpoint_string[8:]

        answers = dns.resolver.resolve("_origin._tcp." + uri, "SRV")
        main_count = 0
        for server in answers:
            print(server.target, server.port, server.priority, server.weight)
            main_count += 1
        assert main_count == 1

        answers = dns.resolver.resolve("_alt0._tcp." + uri, "SRV")
        replica_count = 0
        for server in answers:
            print(server.target, server.port, server.priority, server.weight)

        assert replica_count == 0
