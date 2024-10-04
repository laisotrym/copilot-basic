package com.cmcg.investor.users.services;

import com.cmcg.investor.users.models.Investor;
import java.util.List;

public interface InvestorService {
    List<Investor> getAllInvestors();
    Investor getInvestorById(Long id);
    Investor saveInvestor(Investor investor);
    void deleteInvestor(Long id);
}