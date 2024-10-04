package com.cmcg.investor.users.controllers;

import com.cmcg.investor.users.models.Investor;
import com.cmcg.investor.users.services.InvestorService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/investors")
public class InvestorController {

    @Autowired
    private InvestorService investorService;

    @GetMapping
    public List<Investor> getAllInvestors() {
        return investorService.getAllInvestors();
    }

    @GetMapping("/{id}")
    public Investor getInvestorById(@PathVariable Long id) {
        return investorService.getInvestorById(id);
    }

    @PostMapping
    public Investor createInvestor(@RequestBody Investor investor) {
        return investorService.saveInvestor(investor);
    }

    @PutMapping("/{id}")
    public Investor updateInvestor(@PathVariable Long id, @RequestBody Investor investor) {
        investor.setId(id);
        return investorService.saveInvestor(investor);
    }

    @DeleteMapping("/{id}")
    public void deleteInvestor(@PathVariable Long id) {
        investorService.deleteInvestor(id);
    }
}