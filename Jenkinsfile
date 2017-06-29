pipeline
{
	agent label{'master'}

	options
	{
		buildDiscarder(logRotator(numToKeepStr: '3'))
	}

	stages
	{
		stage('tests')
		{
			steps
			{
				sh 'python helloWorldTest.py'
			}
		}

		stage('run')
		{
			steps
			{
				sh 'python helloWorld.py'
			}
		}

	}
}