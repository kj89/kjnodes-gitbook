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

**live-peers** (30)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,beb10b655c17c4dd306c5afe51b5bcb81ff46e9c@195.128.158.119:26656,48920dc679562d2f116f0b89ac77796377cfb130@194.146.13.254:26656,4da4cae950abf254d747cd24545597ad63cccffc@77.91.72.185:28656,a73bd40070102d04a89de86e7b3fe1c7fbcc394d@89.163.209.3:40656,0108df8793ec07fa82ea202d54b70c603b827ea4@5.9.81.251:60656,f417252166d6508a75371573f3c12e8abca238a5@65.108.108.52:13656,2425a645f1b375c4d61857a7010841d4baf74a1b@109.195.131.79:36656,5a93bbc7e9dc368ccadd2627b35364e0bf06035e@31.187.74.29:26656,e1b25355c160820148744c91d7ec79fea69b18bf@185.144.99.73:26656,c9bd11543948f94d715839d39ae6bfa23deedf74@161.97.78.178:26656,6999cca6c55576a48d4f227b87dc904fbdb085aa@65.21.134.202:26576,6a5846b11911d2c6cf5602f98dafbe68b778ad63@65.109.89.43:40656,2151e36f7696b39147f995c5171805c4eae0788a@194.87.113.40:26656,251c53c762273adbb7853569d17af2a6f00e9c7a@65.108.101.124:13656,8637f94f5cc834d34244a087e370c2ec9b2590bd@75.119.132.90:26656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,6759828432bc76a83d6f8ab5fdd8d045e6035715@46.56.82.104:26656,fb95f32da1b85cb4c1fa04c2e75b045352a5507f@5.104.108.71:26656,4b740c782cc4e6561de519fffb23499f0541e84d@89.116.29.202:18656,2b54651164daac42902f5aff773da59c102333dd@149.102.138.82:26856,c917ffe5d1ca980f75e11aa35f2135b735f9f1a6@143.42.183.90:26656,2931b7010fbbef00c06fd200e26989d903c1a249@89.163.155.252:27656,293806e54d286b72837723eebace872aea21c902@107.155.76.154:26656,0419fefa7d8d3dc13c5689619a9160300a82cf5b@104.238.188.221:40656,e0fe1fd473a399b332280257e53f1fde933b3c5e@109.110.63.204:26656,400370cd7fbd6f0374e6e034676fe4898ef6be29@65.108.103.153:26656,8e6c426f1b0052604cfbc8062e6ee73d3727e945@138.201.21.62:61556,9446504166663fc0090b81abdf86fafe93e72a40@185.209.30.95:40656,d8652a72fa5b61ad82fea2ca3be8b710b56ba88a@38.242.199.69:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
