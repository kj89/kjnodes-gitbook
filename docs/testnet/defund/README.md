# Services

[installation](./installation/ "mention") [upgrade](./upgrade/ "mention") [snapshot](./snapshot/ "mention") [state-sync](./state-sync/ "mention") [useful-commands](./useful-commands/ "mention")

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (30)
```bash
peers="26bdbcbfa286f443c842ed241d35fa09065d586b@161.97.128.243:34656,1a4f0f016ffc8f6814835dc20f5bb7050b2eac90@38.242.239.25:26656,bc934501cffc27940d96e7775b6b8ae5122604ab@185.185.80.195:28656,fee92379b94d5bd81c7af58b6161bce2f10870fe@158.220.104.193:26656,4b740c782cc4e6561de519fffb23499f0541e84d@89.116.29.202:18656,5c2a752c9b1952dbed075c56c600c3a79b58c395@146.59.47.207:26836,beb10b655c17c4dd306c5afe51b5bcb81ff46e9c@195.128.158.119:26656,5a93bbc7e9dc368ccadd2627b35364e0bf06035e@31.187.74.29:26656,48920dc679562d2f116f0b89ac77796377cfb130@194.146.13.254:26656,2151e36f7696b39147f995c5171805c4eae0788a@194.87.113.40:26656,251067e2153905b7da0eab2819c2099c2ed938ae@93.92.205.210:26656,0eb9422efedd714d3db57d1ddfaad75f80a60518@5.161.99.35:26656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,7c459f88962a4d07d7ccd6d0c94f891bb7a7ada0@65.109.26.21:13656,773b4e59036c6934cdd3c919fc74259aba7d8ab3@185.16.39.4:26656,2425a645f1b375c4d61857a7010841d4baf74a1b@109.195.131.79:36656,4da4cae950abf254d747cd24545597ad63cccffc@77.91.72.185:28656,083d01165dd48373b212b25a7d7a811655ce1074@95.111.243.155:26656,6406dc6dff130a009ad79bb04eb29b731414811f@141.95.145.41:27656,efb7323bfefe50b937bb5b9c458ccaa929a17452@23.88.66.239:33656,da77231e4a499106b2fa2f0d64e553c2a9e2203b@65.108.199.206:28656,ed9d651a48968b4c3c8e8f01e15dbb451eed195a@5.75.138.108:26656,e3c348467a8c88c0f65e2ca8a71875d2a384b8b4@185.16.39.19:60656,55d896d8da08838d0d7079b8953c74b7b9519ac1@164.68.127.158:26656,9c9d6b57948fae5cf1c690f3b339ad1200ce0dd2@91.201.112.91:40656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,fb95f32da1b85cb4c1fa04c2e75b045352a5507f@5.104.108.71:26656,0ecf760e856130f9e13bf25300a2f9853c3d58cb@170.187.165.204:26656,6854d36513081c77a24987ab66a436e29e3e5cfa@65.21.131.215:26576,bfef03639bddf4fa503bb75c83af2b5f12c8276c@161.97.155.154:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
