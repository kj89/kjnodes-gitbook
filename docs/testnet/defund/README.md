# Services

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

**live-peers** (28)
```bash
peers="dfa7af21b8c6efebe8aa6028196324f9e0540bbc@94.130.55.76:39656,2425a645f1b375c4d61857a7010841d4baf74a1b@109.195.131.79:36656,48920dc679562d2f116f0b89ac77796377cfb130@194.146.13.254:26656,a73bd40070102d04a89de86e7b3fe1c7fbcc394d@89.163.209.3:40656,1a4f0f016ffc8f6814835dc20f5bb7050b2eac90@38.242.239.25:26656,85b2aa36f9df4d143311fa18745992d5cdd1d0d2@195.2.74.112:40656,15d053c8b58877f598331da4b7851f6faf990fb2@65.109.89.35:26656,beb10b655c17c4dd306c5afe51b5bcb81ff46e9c@195.128.158.119:26656,c917ffe5d1ca980f75e11aa35f2135b735f9f1a6@143.42.183.90:26656,2931b7010fbbef00c06fd200e26989d903c1a249@89.163.155.252:27656,ec35feeccf08262add7748905fba8a6b4f5ae25d@144.91.99.234:30656,faa70500e719bd9a481481a3336a8816810f4f6a@65.109.111.211:16676,13b2cd52bb5d82993ca872b9152ec7d70a811714@136.243.136.241:21656,afdbe2fb845ff591d32f83e4a28b49c59cd9111c@65.109.117.121:13656,773b4e59036c6934cdd3c919fc74259aba7d8ab3@185.16.39.4:26656,2151e36f7696b39147f995c5171805c4eae0788a@194.87.113.40:26656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,6759828432bc76a83d6f8ab5fdd8d045e6035715@46.56.82.104:26656,4b740c782cc4e6561de519fffb23499f0541e84d@89.116.29.202:18656,8e039627e5fe9f829b20a71d93ba40e015d0a0d5@135.181.128.249:26656,400370cd7fbd6f0374e6e034676fe4898ef6be29@65.108.103.153:26656,8f607938d46808af7263dd4befcdc5fcaeedccb4@194.163.165.216:40656,fb95f32da1b85cb4c1fa04c2e75b045352a5507f@5.104.108.71:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,6448d127ec3b31a1565603409c327699ff9c0b52@77.91.78.222:26656,7c459f88962a4d07d7ccd6d0c94f891bb7a7ada0@65.109.26.21:13656,e0ab16d47276dee411fc01abc86c787d95ef6aba@65.109.111.204:29656,0634c78898f78ff7d526c233be4e82ab7e3ad824@167.86.91.114:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
