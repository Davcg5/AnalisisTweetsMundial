package tweetsPorHora;

import java.awt.Color;
import java.io.File;
import java.io.IOException;

import javax.swing.JFrame;
import javax.swing.JPanel;

import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartFrame;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.ChartUtilities;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.CategoryPlot;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.category.DefaultCategoryDataset;


public class GraficoHoras extends JFrame{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	

	public static void main(String args[]){
		ObtencionDatosHoras OD = new ObtencionDatosHoras();
		OD.pais1();
		OD.pais2();
		
		new GraficoHoras().setVisible(true);
		// Fuente de Datos
		DefaultCategoryDataset dataset = new DefaultCategoryDataset();
		
		dataset.setValue(ObtencionDatosHoras.horas2.get("01  "), ObtencionDatosHoras.tweetsPais1, "01");
		dataset.setValue(ObtencionDatosHoras.horas.get("01  "), ObtencionDatosHoras.tweetsPais2, "01");
		dataset.setValue(ObtencionDatosHoras.horas2.get("02  "), ObtencionDatosHoras.tweetsPais1, "02");
		dataset.setValue(ObtencionDatosHoras.horas.get("02  "), ObtencionDatosHoras.tweetsPais2, "02");
		dataset.setValue(ObtencionDatosHoras.horas2.get("03  "), ObtencionDatosHoras.tweetsPais1, "03");
		dataset.setValue(ObtencionDatosHoras.horas.get("03  "), ObtencionDatosHoras.tweetsPais2, "03");
		dataset.setValue(ObtencionDatosHoras.horas2.get("04  "), ObtencionDatosHoras.tweetsPais1, "04");
		dataset.setValue(ObtencionDatosHoras.horas.get("04  "), ObtencionDatosHoras.tweetsPais2, "04");
		dataset.setValue(ObtencionDatosHoras.horas2.get("05  "), ObtencionDatosHoras.tweetsPais1, "05");
		dataset.setValue(ObtencionDatosHoras.horas.get("05  "), ObtencionDatosHoras.tweetsPais2, "05");
		dataset.setValue(ObtencionDatosHoras.horas2.get("06  "), ObtencionDatosHoras.tweetsPais1, "06");
		dataset.setValue(ObtencionDatosHoras.horas.get("06  "), ObtencionDatosHoras.tweetsPais2, "06");
		dataset.setValue(ObtencionDatosHoras.horas2.get("07  "), ObtencionDatosHoras.tweetsPais1, "07");
		dataset.setValue(ObtencionDatosHoras.horas.get("07  "), ObtencionDatosHoras.tweetsPais2, "07");
		dataset.setValue(ObtencionDatosHoras.horas2.get("08  "), ObtencionDatosHoras.tweetsPais1, "08");
		dataset.setValue(ObtencionDatosHoras.horas.get("08  "), ObtencionDatosHoras.tweetsPais2, "08");
		dataset.setValue(ObtencionDatosHoras.horas2.get("09  "), ObtencionDatosHoras.tweetsPais1, "09");
		dataset.setValue(ObtencionDatosHoras.horas.get("09  "), ObtencionDatosHoras.tweetsPais2, "09");
		dataset.setValue(ObtencionDatosHoras.horas2.get("10  "), ObtencionDatosHoras.tweetsPais1, "10");
		dataset.setValue(ObtencionDatosHoras.horas.get("10  "), ObtencionDatosHoras.tweetsPais2, "10");
		dataset.setValue(ObtencionDatosHoras.horas2.get("11  "), ObtencionDatosHoras.tweetsPais1, "11");
		dataset.setValue(ObtencionDatosHoras.horas.get("11  "), ObtencionDatosHoras.tweetsPais2, "11");
		dataset.setValue(ObtencionDatosHoras.horas2.get("12  "), ObtencionDatosHoras.tweetsPais1, "12");
		dataset.setValue(ObtencionDatosHoras.horas.get("12  "), ObtencionDatosHoras.tweetsPais2, "12");
		dataset.setValue(ObtencionDatosHoras.horas2.get("13  "), ObtencionDatosHoras.tweetsPais1, "13");
		dataset.setValue(ObtencionDatosHoras.horas.get("13  "), ObtencionDatosHoras.tweetsPais2, "13");
		dataset.setValue(ObtencionDatosHoras.horas2.get("14  "), ObtencionDatosHoras.tweetsPais1, "14");
		dataset.setValue(ObtencionDatosHoras.horas.get("14  "), ObtencionDatosHoras.tweetsPais2, "14");
		dataset.setValue(ObtencionDatosHoras.horas2.get("15  "), ObtencionDatosHoras.tweetsPais1, "15");
		dataset.setValue(ObtencionDatosHoras.horas.get("15  "), ObtencionDatosHoras.tweetsPais2, "15");
		dataset.setValue(ObtencionDatosHoras.horas2.get("16  "), ObtencionDatosHoras.tweetsPais1, "16");
		dataset.setValue(ObtencionDatosHoras.horas.get("16  "), ObtencionDatosHoras.tweetsPais2, "16");
		dataset.setValue(ObtencionDatosHoras.horas2.get("17  "), ObtencionDatosHoras.tweetsPais1, "17");
		dataset.setValue(ObtencionDatosHoras.horas.get("17  "), ObtencionDatosHoras.tweetsPais2, "17");
		dataset.setValue(ObtencionDatosHoras.horas2.get("18  "), ObtencionDatosHoras.tweetsPais1, "18");
		dataset.setValue(ObtencionDatosHoras.horas.get("18  "), ObtencionDatosHoras.tweetsPais2, "18");
		dataset.setValue(ObtencionDatosHoras.horas2.get("19  "), ObtencionDatosHoras.tweetsPais1, "19");
		dataset.setValue(ObtencionDatosHoras.horas.get("19  "), ObtencionDatosHoras.tweetsPais2, "19");
		dataset.setValue(ObtencionDatosHoras.horas2.get("20  "), ObtencionDatosHoras.tweetsPais1, "20");
		dataset.setValue(ObtencionDatosHoras.horas.get("20  "), ObtencionDatosHoras.tweetsPais2, "20");
		dataset.setValue(ObtencionDatosHoras.horas2.get("21  "), ObtencionDatosHoras.tweetsPais1, "21");
		dataset.setValue(ObtencionDatosHoras.horas.get("21  "), ObtencionDatosHoras.tweetsPais2, "21");
		dataset.setValue(ObtencionDatosHoras.horas2.get("22  "), ObtencionDatosHoras.tweetsPais1, "22");
		dataset.setValue(ObtencionDatosHoras.horas.get("22  "), ObtencionDatosHoras.tweetsPais2, "22");
		dataset.setValue(ObtencionDatosHoras.horas2.get("23  "), ObtencionDatosHoras.tweetsPais1, "23");
		dataset.setValue(ObtencionDatosHoras.horas.get("23  "), ObtencionDatosHoras.tweetsPais2, "23");
		
		// Creando el Grafico
		JFreeChart chart = ChartFactory.createBarChart3D
				("Tweets","Hora", "Numero", 
						dataset, PlotOrientation.VERTICAL, true,true, false);
		chart.setBackgroundPaint(Color.white);
		chart.getTitle().setPaint(Color.black); 
		CategoryPlot p = chart.getCategoryPlot(); 
		p.setRangeGridlinePaint(Color.gray); 
		// Mostrar Grafico
		ChartPanel chartPanel = new ChartPanel(chart);
		   ChartFrame frame = new ChartFrame("JFreeChart", chart);
	        frame.pack();
	        frame.setVisible(true);
		try {

			ChartUtilities.saveChartAsJPEG(new File("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\BELVSJAPHoras.jpg"), chart, 1500, 1500);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}
}
