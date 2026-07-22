class ResponseManager:

    def show(self, response):

        if response.success:

            print(f"\n🤖 Jarvis: {response.message}")

        else:

            print(f"\n❌ Jarvis: {response.message}")