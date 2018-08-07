package Sentimientos;


import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Hashtable;


public class ObtencionDatosSentimientos {

	static String Pais1;
	static String Pais2;
	static int tweetsPais1= 0;
	static int tweetsPais2= 0;

	static String ndeTweets1; 
	static String ndeTweets2;
	static Hashtable<String, Integer> sentimientosPais2 = new Hashtable<String, Integer>();
	static Hashtable<String, Integer> sentimientosPais1 = new Hashtable<String, Integer>();
	public static void pais1(){
		
		File file = new File("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\sentimientosBra.txt");
		FileReader fileR = null;
		BufferedReader file2 = null;

		try {
			fileR = new FileReader(file);
			file2 = new BufferedReader(fileR);
			String name = file.getName();
			 Pais1 = name.substring(name.length() - 7, name.length()-3);
			System.out.println(Pais1);
		
		} catch (FileNotFoundException e) {
			System.out.println("No se encontro el archivo "+file.getName());

		}

		try {
			String lines = "";
			int valor =0;
			while( ( lines = file2.readLine()) != null) {
				//System.out.println(lines.charAt(0));
				
				String[] partes = lines.split(",");
				
			
				if (sentimientosPais1.get(partes[0])== null){
					sentimientosPais1.put(partes[0], 1);
					
				}
				else{
				valor = sentimientosPais1.get(partes[0]) ;
				valor = valor +1;
				sentimientosPais1.put(partes[0], valor);
				}
				


			}
			tweetsPais1 =sentimientosPais1.get("positive  ")+ sentimientosPais1.get("negative  ")+sentimientosPais1.get("neutral  ");
			ndeTweets1 = Pais1 + ":" + String.valueOf(tweetsPais1);
			System.out.println(tweetsPais1);
		}catch (IOException e) {
			e.printStackTrace();
		}
	}

	public static void pais2(){
		
		File file = new File("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\sentimientosMex.txt");
		FileReader fileR = null;
		BufferedReader file2 = null;

		try {
			fileR = new FileReader(file);
			file2 = new BufferedReader(fileR);
			String name = file.getName();
			 Pais2 = name.substring(name.length() - 7, name.length()-3);
			System.out.println(Pais2);

		} catch (FileNotFoundException e) {
			System.out.println("No se encontro el archivo "+file.getName());

		}

		try {
			String lines = "";
			int valor =0;
			
			while( ( lines = file2.readLine()) != null) {
				//System.out.println(lines.charAt(0));
				
				String[] partes = lines.split(",");
				
				if (sentimientosPais2.get(partes[0])== null){
					sentimientosPais2.put(partes[0], 1);
				}
				else{
				valor = sentimientosPais2.get(partes[0]) ;
				valor = valor +1;
				sentimientosPais2.put(partes[0], valor);
				}
				
				

			}
			tweetsPais2 =sentimientosPais2.get("positive  ")+ sentimientosPais2.get("negative  ")+sentimientosPais2.get("neutral  ");
			System.out.println(sentimientosPais2 + "espacio" + sentimientosPais1);
			ndeTweets2 = Pais2 + ":" + String.valueOf(tweetsPais2);
			System.out.print (tweetsPais2);
		}catch (IOException e) {
			e.printStackTrace();
		}
	}
}



