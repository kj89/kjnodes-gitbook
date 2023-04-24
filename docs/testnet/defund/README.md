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

**live-peers** (29)
```bash
peers="8130e6090c692e7f43ba0b155f752251242314d2@83.167.103.215:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,70c35e37f399fe02d41823c97188a4e5911d5b17@38.242.217.231:26656,da77231e4a499106b2fa2f0d64e553c2a9e2203b@65.108.199.206:28656,1f4fba40d21d0b22cb7e7ec3972bccd3473e5972@86.102.123.237:26656,72b1ac46a6924e6cb39c086cfec8da7b61d93ff6@38.242.139.98:26656,2151e36f7696b39147f995c5171805c4eae0788a@194.87.113.40:26656,1a4f0f016ffc8f6814835dc20f5bb7050b2eac90@38.242.239.25:26656,acdac8b95e2fbe003101bda9e123d3a52951696c@62.171.143.40:26656,492f8fbaf5270cf739941979593757bea7bc8549@116.202.241.157:10156,86caf6297ae00fb58b58a272984275c592b2fdf7@65.109.84.216:56656,07b192c0216a0f8361f1271e56c0413b9638e372@194.35.120.237:26656,4da4cae950abf254d747cd24545597ad63cccffc@77.91.72.185:28656,fb76c9e69a87c0ffb2bbcd2adaa29b8c59a9698a@195.74.86.11:26656,2e85746b14e83108c991ef0f9f55c291f5e7d6a9@88.198.18.24:13656,e1b25355c160820148744c91d7ec79fea69b18bf@185.144.99.73:26656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,2609c228430dbb4652a62d17c09187a6ee831bff@188.233.19.198:26656,2931b7010fbbef00c06fd200e26989d903c1a249@89.163.155.252:27656,73c4f0b46f8e6b013980ddb5196932b00b09106f@94.103.91.211:40656,cee0d215e82cadb63f7067c8d0d7848cb24f034d@65.109.25.58:13656,bda598af0c96d72a85c3b6840138d929b8c4e762@84.46.248.207:26656,d0c6f2febf03bbf69a3cd1c5fb489d7febfc34b9@65.109.116.119:40656,8637f94f5cc834d34244a087e370c2ec9b2590bd@75.119.132.90:26656,9f8028ece9c514cf8f2646f8d968480b3341149f@157.90.25.62:26656,8f607938d46808af7263dd4befcdc5fcaeedccb4@194.163.165.216:40656,cdcd6ba08042b31391492666da593cc80d198cab@84.54.23.85:26656,002422812948a68fe851bed557de2d0040d41e06@31.220.80.134:30656,e3f55bcaf4a7f24ab192dcdd8d55a2c91a0a4003@46.216.183.171:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
