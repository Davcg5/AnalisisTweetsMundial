package Sentimientos;

import java.io.File;
import java.io.IOException;

import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartFrame;
import org.jfree.chart.ChartUtilities;
import org.jfree.chart.JFreeChart;
import org.jfree.data.general.DefaultPieDataset;

import tweetsporfecha.GraficoFecha;
import tweetsporfecha.ObtencionDatosFecha;

public class GraficoSentimientos {
	static String cadena= "" ;
	public static void main(String args[]){
        // Fuente de Datos
		ObtencionDatosSentimientos OD = new ObtencionDatosSentimientos();
		OD.pais1();
		OD.pais2();
        DefaultPieDataset data = new DefaultPieDataset();
        data.setValue("positivos"+ ObtencionDatosSentimientos.Pais1+ ":"+String.valueOf(ObtencionDatosSentimientos.sentimientosPais1.get("positive  ")), ObtencionDatosSentimientos.sentimientosPais1.get("positive  "));
        data.setValue("negativos"+ ObtencionDatosSentimientos.Pais1+ ":" +String.valueOf(ObtencionDatosSentimientos.sentimientosPais1.get("negative  ")), ObtencionDatosSentimientos.sentimientosPais1.get("negative  "));
        data.setValue("neutral "+ ObtencionDatosSentimientos.Pais1+ ":"+String.valueOf(ObtencionDatosSentimientos.sentimientosPais1.get("neutral  ")), ObtencionDatosSentimientos.sentimientosPais1.get("neutral  "));
        data.setValue("positivos "+ ObtencionDatosSentimientos.Pais2+ ":" +String.valueOf(ObtencionDatosSentimientos.sentimientosPais2.get("positive  ")), ObtencionDatosSentimientos.sentimientosPais2.get("positive  "));
        data.setValue("neutral "+ ObtencionDatosSentimientos.Pais2+ ":" +String.valueOf(ObtencionDatosSentimientos.sentimientosPais2.get("negative  ")), ObtencionDatosSentimientos.sentimientosPais2.get("negative  "));
        data.setValue("negativos "+ ObtencionDatosSentimientos.Pais2+ ":"+String.valueOf(ObtencionDatosSentimientos.sentimientosPais2.get("neutral  ")), ObtencionDatosSentimientos.sentimientosPais2.get("neutral  "));
        // Creando el Grafico
        JFreeChart chart = ChartFactory.createPieChart(
        		ObtencionDatosSentimientos.ndeTweets1 + "||"+ObtencionDatosSentimientos.ndeTweets2, 
         data, 
         true, 
         true, 
         false);
 
        // Mostrar Grafico
        ChartFrame frame = new ChartFrame("JFreeChart", chart);
        frame.pack();
        frame.setVisible(true);
    	
    	try {

			ChartUtilities.saveChartAsJPEG(new File("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\INGVSBELSentimientos.jpg"), chart, 1500, 1500);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	
    }
}

