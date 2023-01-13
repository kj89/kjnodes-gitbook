# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-3 | **Latest Version Tag**: v0.2.1 | **Wasm**: OFF

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)


## Public endpoints

* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)

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

**live-peers** (38)
```bash
peers="5db1142851dd1c7106779aa9d348a9f67a630df0@164.68.110.234:26656,58437bc62307a512f391db5c1e24e3cff8b9f8d3@136.243.88.91:2070,36909ce5289d8f994fb2562f7a188a79ce826359@141.95.145.41:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,a28ed6c0af36097350181d5fa2d116f6e93585fe@38.242.139.91:26656,09f8d04b89d6ed15e216a4c7f5469f42d5b90f9b@195.201.241.25:40656,4725abd8d2a813dce5c90f0bc36bb8f9260fc9cc@82.208.20.248:26656,ccace1585ce7d671f09d4d442d77936b29ee8118@164.68.127.182:26656,8809c1c07534b5fc6802eecdc810c5a39263e6b5@45.140.147.117:26656,9e67baeac323278617e9036a892464b21dfe3a38@65.108.71.92:45656,65f62492afbf35d8aade01c4abe97d72634459c4@65.109.84.254:26656,71b1aceddd8b697c5e5ce22aee60ff1e1c5f20c5@176.124.222.160:26656,7831e762e13c2cb99236b59f5513bf1f8d16d036@88.99.3.158:10356,5e6354412f3742ac76e37838236707b373c1de43@185.250.37.162:29656,4eb0bef7997b87086c40766193d812479238187c@217.76.55.66:26656,9cbaf117258ac247bce37f314d1a2ddba34b5ad6@194.163.190.54:26656,e4470dac98f2cee5bd060c52c7d801d57bfc9308@185.245.182.206:26656,2ef97b017d5ef592d52aba8672610b38680f993b@161.97.78.40:26656,b1c64cdd7bd0f798eaa0239fd0cee26e770628b3@194.233.82.172:29656,2b76e96658f5e5a5130bc96d63f016073579b72d@51.91.215.40:45656,2c57fc71ccb618acd7823422afaa78bffb8550cd@65.109.93.152:31256,3e32ecfc9b0eaf146d8648735f4da2f423c5a87d@84.46.250.215:26656,cd53ab15aa53f7fd0f584bb60b253a4d53246867@93.189.30.116:26656,2cb1c2f09299b8a2c3ae1614782733e29d72b9ce@178.211.139.124:40656,ef4cac7e5813a753239239e297efcabc03a07fbb@194.180.176.125:26656,fd6631cb2d3c2b035f13279c5970ba6a858d0d30@95.216.222.177:34656,1a2166e8c08130d678cae0bc88cfabc8b6ed8d78@178.18.244.17:26656,7ca31e50d5509104ea481869bcbe91e6883fe9d0@135.181.150.198:36656,58d46050cf77065d27e9526a7e93c8f814cc036a@194.146.13.185:26656,d9695d9eec0915e165824258f4f97c23ae761da6@194.4.48.96:26656,95778d4f8da28dcec38be627c0a6b8e513f91f30@155.133.22.130:26656,1fa66a7b70a45fa6ca9aa215124587bca4e1da7b@167.235.203.235:26656,8edfd82e69ea3c7ddca4e0a88e2d63f33501c8ea@75.119.154.72:26656,d49ed18a1c3ada861668d8ad391bbc66f4e41b4e@194.146.13.189:26656,834b6b2cf3934f5b38279dc1d00d4c8f8231272b@176.126.87.84:26656,aee64a0d9b4f06f9f0949650fa22494b1cee1d58@84.46.244.228:26656,fadb50dd153e127fbd56b7a4823beb355d4c103b@217.76.55.73:26656,7bd385047301b8a0caee30f9b99faa3e511c35e3@38.242.142.76:40656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
