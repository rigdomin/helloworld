pipeline
{
	agent any

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
				sh 'python src/helloWorldTest.py'
			}
		}

		stage('run')
		{
			steps
			{
				sh 'python submissions/helloWorld.py'
			}
		}

	}
}