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

**live-peers** (28)
```bash
peers="c88bb696ecc88c3175312d04c5e3a8e2f64a3835@194.163.168.94:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,6448d127ec3b31a1565603409c327699ff9c0b52@77.91.78.222:26656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@146.59.47.207:26836,2425a645f1b375c4d61857a7010841d4baf74a1b@109.195.131.79:36656,8274cf9149b23c23694cdce7045a607879fc51b2@95.217.182.26:26456,beb10b655c17c4dd306c5afe51b5bcb81ff46e9c@195.128.158.119:26656,2151e36f7696b39147f995c5171805c4eae0788a@194.87.113.40:26656,15f51735fd76f72abfca70f4bb2da93458b63073@93.100.235.162:26656,2931b7010fbbef00c06fd200e26989d903c1a249@89.163.155.252:27656,da77231e4a499106b2fa2f0d64e553c2a9e2203b@65.108.199.206:28656,4b740c782cc4e6561de519fffb23499f0541e84d@89.116.29.202:18656,78ae69a09315cb1d22b260f9f526b2f609c7a215@65.108.10.22:46656,d7b1896a0dad8f7c5d77cb8656271c972120ce55@154.53.54.154:30656,4367e2b815008789932148f8af1b720ed7c89d85@84.54.192.204:26656,f417252166d6508a75371573f3c12e8abca238a5@65.108.108.52:13656,e2803c99090a9b406c646a3b8ae3dcb8d2dfaf07@65.109.83.24:26656,fb95f32da1b85cb4c1fa04c2e75b045352a5507f@5.104.108.71:26656,6406dc6dff130a009ad79bb04eb29b731414811f@141.95.145.41:27656,48920dc679562d2f116f0b89ac77796377cfb130@194.146.13.254:26656,ad644354fe8141fd01250f186fe2abd11453c6d7@185.209.223.44:40656,206310423b4a8e09115d824bee3a6595d93d86c8@89.163.151.193:26656,3c941829d9c2ce59a0cf12bd0d1ef8dd5db8c6c3@178.163.77.190:26656,854cfaf6fd4de846fd020fbd7d0b5364c6fb9c58@65.21.95.46:27656,8637f94f5cc834d34244a087e370c2ec9b2590bd@75.119.132.90:26656,64db984bc93ab23b3a1e2d8f060b56f1ef596b51@178.124.209.101:26656,7c459f88962a4d07d7ccd6d0c94f891bb7a7ada0@65.109.26.21:13656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
