package com.ohprice.poc;

import com.ohprice.poc.controller.Controller;
import com.ohprice.poc.model.Model;
import com.ohprice.poc.view.View;

import javax.swing.*;

/**
 * Simple Swing App using MVC pattern
 * @author Ola Ajibode
 */
public class App {
    public static void main(String[] args) {
        System.out.println("Loading the Swing Application.....");
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                runApp();
            }

        });


    }

    public static void runApp() {
        System.out.println("App runner in progress");
        Model model = new Model();
        View view = new View(model);
        Controller controller = new Controller(model, view);
    }


}
