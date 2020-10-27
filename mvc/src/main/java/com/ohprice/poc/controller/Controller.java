package com.ohprice.poc.controller;

import com.ohprice.poc.model.Model;
import com.ohprice.poc.view.View;

public class Controller {
    private Model model;
    private View view;

    public Controller(Model model, View view) {
        this.model = model;
        this.view = view;
    }
}
