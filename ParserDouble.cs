using System;
using System.Collections;
using System.IO;

namespace ScannerParser
{

	public class Parser
	{

		const int maxToken = 14;


		public static Token LastToken;
		public static Token LookAheadToken;
		private static int MaxErrors = 5;
		private static int CurrentErrors=0;

		
			/*--------------Scanner Especification----------*/


		private static void SynError(int n)
		{
			if(CurrentErrors<MaxErrors)
			{
				Errors.SynError(LookAheadToken.Line, LookAheadToken.Col, n);
				CurrentErrors++;
			}
		}
		
		private static void Get()
		{
			LastToken = LookAheadToken;
			LookAheadToken = Scanner.Scan();
			
			while(LookAheadToken.Kind>maxToken)
			{
				LastToken = LookAheadToken;
				LookAheadToken = Scanner.Scan();
			}
		}
		
		private static void Expect(int n)
		{
			if(LookAheadToken.Kind==n)
			{Get();}
			else
			{SynError(n);}
		}
		


		public static void Expr()
		{
			
			while(LookAheadToken.Kind==7 || LookAheadToken.Kind==1 || LookAheadToken.Kind==2 || LookAheadToken.Kind==10)
			{
				Stat();
				
				Expect(4);
				 
				
				while(LookAheadToken.Kind==3)
				{
					Expect(3);
					
				}
				 
				
			}

			while(LookAheadToken.Kind==3)
			{
				Expect(3);
				
			}

			Expect(5);
			  
			
		}


		public static void Stat()
		{
			double value=0;
			
			Expression(ref value);
			System.Console.WriteLine("Resultado: {0}",value);
			
		}


		public static void Expression(ref double result)
		{
			double result1=0,result2=0;
			
			Term(ref result1);
			
			while(LookAheadToken.Kind==6 || LookAheadToken.Kind==7)
			{
				switch(LookAheadToken.Kind)
				{
					case 6:
											
						Expect(6);
						
						Term(ref result2);
						result1+=result2;  
						
						break;
					case 7:
											
						Expect(7);
						
						Term(ref result2);
						result1-=result2;  
						
						break;
					default:
						SynError(16);
						break;

				}
			}
			result=result1; 
			
		}


		public static void Term(ref double result)
		{
			double result1=0,result2=0;
			
			Factor(ref result1);
			
			while(LookAheadToken.Kind==8 || LookAheadToken.Kind==9)
			{
				switch(LookAheadToken.Kind)
				{
					case 8:
											
						Expect(8);
						
						Factor(ref result2);
						result1*=result2;  
						
						break;
					case 9:
											
						Expect(9);
						
						Factor(ref result2);
						result1/=result2;  
						
						break;
					default:
						SynError(17);
						break;

				}
			}
			result=result1; 
			
		}


		public static void Factor(ref double result)
		{
			double sign=1;
			
			switch(LookAheadToken.Kind)
			{
				case 7:
									
					Expect(7);
					sign = -1; 
					
					break;
													
			}
			switch(LookAheadToken.Kind)
			{
				case 1:
				case 2:
									
					Number(ref result);
					 result*=sign;
					
					break;
				case 10:
									
					Expect(10);
					
					Expression(ref result);
					 
					
					Expect(11);
					  result*=sign;
					
					break;
				default:
					SynError(18);
					break;

			}
		}


		public static void Number(ref double result)
		{
			
			switch(LookAheadToken.Kind)
			{
				case 1:
									
					Expect(1);
					 result = double.Parse(LastToken.Value);
					
					break;
				case 2:
									
					Expect(2);
					 result = double.Parse(LastToken.Value);
					
					break;
				default:
					SynError(19);
					break;

			}
		}



		public static void Parse()
		{
			LookAheadToken = new Token();
			LookAheadToken.Value = new string(' ',0);
			Get();
				Expr();

			Expect(0);
		}
	
	}//END PARSER


	public class Errors
	{
		public static int Count=0;
		public static string ErrMsgFormat = "Error Line {0} Col {1}: {2}";
		
		public static void SynError(int Line, int Col, int n)
		{
			string Error = new string(' ',0);
			switch(n)
			{
				case 0:
					Error = "EOF Invalid";
					break;
				case 1:
					Error = "number Expected";
					break;
				case 2:
					Error = "decnumber Expected";
					break;
				case 3:
					Error = "white Expected";
					break;
				case 4:
					Error = "; Expected";
					break;
				case 5:
					Error = ". Expected";
					break;
				case 6:
					Error = "+ Expected";
					break;
				case 7:
					Error = "- Expected";
					break;
				case 8:
					Error = "* Expected";
					break;
				case 9:
					Error = "/ Expected";
					break;
				case 10:
					Error = "( Expected";
					break;
				case 11:
					Error = ") Expected";
					break;
				case 12:
					Error = "while Expected";
					break;
				case 13:
					Error = "do Expected";
					break;
				case 14:
					Error = "Expr Invalid";
					break;
				case 15:
					Error = "Stat Invalid";
					break;
				case 16:
					Error = "Expression Invalid";
					break;
				case 17:
					Error = "Term Invalid";
					break;
				case 18:
					Error = "Factor Invalid";
					break;
				case 19:
					Error = "Number Invalid";
					break;

				default:
					Error = "Error desconocido: " + n.ToString();
					break;
			}	
			Console.WriteLine(ErrMsgFormat,Line,Col,Error);
			Count++;
		}
	
	}//END ERRORS

}//END NAMESPACE

