# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/defund.png" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: orbit-alpha-1 | **Latest Version Tag**: v0.2.6 | **Wasm**: ON

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/defund-testnet](https://explorer.kjnodes.com/defund-testnet)

## Public endpoints

* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)
* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* grpc: defund-testnet.grpc.kjnodes.com:40090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (29)
```bash
peers="d1a68b360ef45ac1a90f047a9e3c81510aee5490@89.163.142.196:40656,2425a645f1b375c4d61857a7010841d4baf74a1b@109.195.131.79:36656,dfa7af21b8c6efebe8aa6028196324f9e0540bbc@94.130.55.76:39656,beb10b655c17c4dd306c5afe51b5bcb81ff46e9c@195.128.158.119:26656,d0c6f2febf03bbf69a3cd1c5fb489d7febfc34b9@65.109.116.119:40656,070c34fcc9ca8460ee6313725d76404153e5b850@65.108.250.35:40656,03f305b8efa44ed1520e73656029aeb144312505@94.231.131.216:26656,8274cf9149b23c23694cdce7045a607879fc51b2@95.217.182.26:26456,181e8b5bb6e2e3495c030429e0e696ef666f9117@65.109.144.236:27656,2151e36f7696b39147f995c5171805c4eae0788a@194.87.113.40:26656,aee8438ae38fe7819da2dcecd61895476ea6d651@95.217.89.52:13656,fb95f32da1b85cb4c1fa04c2e75b045352a5507f@5.104.108.71:26656,6b9797483562f7836e0ab23e63b911daf324b55d@65.108.238.147:28656,1c1168470ca6c5cbdab483335a7532a1a8716c3e@65.21.183.56:26656,4b740c782cc4e6561de519fffb23499f0541e84d@89.116.29.202:18656,ad644354fe8141fd01250f186fe2abd11453c6d7@185.209.223.44:40656,0eb9422efedd714d3db57d1ddfaad75f80a60518@5.161.99.35:26656,cdcd6ba08042b31391492666da593cc80d198cab@84.54.23.85:26656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,5a93bbc7e9dc368ccadd2627b35364e0bf06035e@31.187.74.29:26656,2a2e46081bc82ac711df8e54159004440de6bcc4@65.109.116.50:33656,5c2a752c9b1952dbed075c56c600c3a79b58c395@146.59.47.207:26836,878c7b70a38f041d49928dc02418619f85eecbf6@65.109.18.166:45656,2931b7010fbbef00c06fd200e26989d903c1a249@89.163.155.252:27656,773b4e59036c6934cdd3c919fc74259aba7d8ab3@185.16.39.4:26656,944fd51f8539f77a3d1b2eac781c2f1da62568ca@65.109.70.168:36656,15d053c8b58877f598331da4b7851f6faf990fb2@65.109.89.35:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,bfef03639bddf4fa503bb75c83af2b5f12c8276c@161.97.155.154:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
