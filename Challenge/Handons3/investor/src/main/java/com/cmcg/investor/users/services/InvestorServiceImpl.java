package com.cmcg.investor.users.services;

import com.cmcg.investor.users.models.Investor;
import com.cmcg.investor.users.repositories.InvestorRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class InvestorServiceImpl implements InvestorService {

    @Autowired
    private InvestorRepository investorRepository;

    @Override
    public List<Investor> getAllInvestors() {
        return investorRepository.findAll();
    }

    @Override
    public Investor getInvestorById(Long id) {
        return investorRepository.findById(id).orElse(null);
    }

    @Override
    public Investor saveInvestor(Investor investor) {
        return investorRepository.save(investor);
    }

    @Override
    public void deleteInvestor(Long id) {
        investorRepository.deleteById(id);
    }
}