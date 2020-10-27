package com.ohprice.poc.view;

import com.ohprice.poc.model.Model;

import javax.swing.*;
import java.awt.*;

public class View extends JFrame {

    private Model model;

    public View(Model model) throws HeadlessException {
        super("MVC Demo App");
        this.model = model;


    }
}
