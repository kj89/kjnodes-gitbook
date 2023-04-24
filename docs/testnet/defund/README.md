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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,c24e38e2bf28f81a6935110c07cdeb95f5765ed1@65.109.84.254:26656,48920dc679562d2f116f0b89ac77796377cfb130@194.146.13.254:26656,5a93bbc7e9dc368ccadd2627b35364e0bf06035e@31.187.74.29:26656,492f8fbaf5270cf739941979593757bea7bc8549@116.202.241.157:10156,85b2aa36f9df4d143311fa18745992d5cdd1d0d2@195.2.74.112:40656,2609c228430dbb4652a62d17c09187a6ee831bff@188.233.19.198:26656,7c459f88962a4d07d7ccd6d0c94f891bb7a7ada0@65.109.26.21:13656,ed9d651a48968b4c3c8e8f01e15dbb451eed195a@5.75.138.108:26656,4b740c782cc4e6561de519fffb23499f0541e84d@89.116.29.202:18656,31fc276eaba0046da7f770c60897bf4131e0db63@95.165.107.241:28656,8130e6090c692e7f43ba0b155f752251242314d2@83.167.103.215:26656,da77231e4a499106b2fa2f0d64e553c2a9e2203b@65.108.199.206:28656,cdcd6ba08042b31391492666da593cc80d198cab@84.54.23.85:26656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,2e85746b14e83108c991ef0f9f55c291f5e7d6a9@88.198.18.24:13656,2151e36f7696b39147f995c5171805c4eae0788a@194.87.113.40:26656,e1b25355c160820148744c91d7ec79fea69b18bf@185.144.99.73:26656,1f993dfcf30d91c15437e8657b6020aea07f7632@65.108.232.182:13656,1f4fba40d21d0b22cb7e7ec3972bccd3473e5972@86.102.123.237:26656,445bebcbfc243bf78c3a2616bff0eedc5e4b6797@95.171.21.43:26656,8637f94f5cc834d34244a087e370c2ec9b2590bd@75.119.132.90:26656,2931b7010fbbef00c06fd200e26989d903c1a249@89.163.155.252:27656,4da4cae950abf254d747cd24545597ad63cccffc@77.91.72.185:28656,6406dc6dff130a009ad79bb04eb29b731414811f@141.95.145.41:27656,acdac8b95e2fbe003101bda9e123d3a52951696c@62.171.143.40:26656,86caf6297ae00fb58b58a272984275c592b2fdf7@65.109.84.216:56656,6999cca6c55576a48d4f227b87dc904fbdb085aa@65.21.134.202:26576,9f8028ece9c514cf8f2646f8d968480b3341149f@157.90.25.62:26656,bc3d614b684c8e1647f4196dc8a785b1ab0381ef@65.108.13.154:33656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
