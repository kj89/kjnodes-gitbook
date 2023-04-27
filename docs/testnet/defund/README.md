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

**live-peers** (27)
```bash
peers="2425a645f1b375c4d61857a7010841d4baf74a1b@109.195.131.79:36656,4f1d96f5b8adb5bcdd59e61cb6e387ff12422a41@65.109.63.110:13656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,4b740c782cc4e6561de519fffb23499f0541e84d@89.116.29.202:18656,944fd51f8539f77a3d1b2eac781c2f1da62568ca@65.109.70.168:36656,beb10b655c17c4dd306c5afe51b5bcb81ff46e9c@195.128.158.119:26656,48920dc679562d2f116f0b89ac77796377cfb130@194.146.13.254:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,2151e36f7696b39147f995c5171805c4eae0788a@194.87.113.40:26656,8f607938d46808af7263dd4befcdc5fcaeedccb4@194.163.165.216:40656,8637f94f5cc834d34244a087e370c2ec9b2590bd@75.119.132.90:26656,fb95f32da1b85cb4c1fa04c2e75b045352a5507f@5.104.108.71:26656,5a93bbc7e9dc368ccadd2627b35364e0bf06035e@31.187.74.29:26656,c9bd11543948f94d715839d39ae6bfa23deedf74@161.97.78.178:26656,34b72721aa503574a0709b1859fb1da2aa12ce70@88.99.3.158:11256,4da4cae950abf254d747cd24545597ad63cccffc@77.91.72.185:28656,28e18559a10e257e80a79730731fe3d0d03a8f52@79.137.248.29:40656,f417252166d6508a75371573f3c12e8abca238a5@65.108.108.52:13656,f968e0c25141ecde67edfa85a0ebdc5113ebcbea@135.181.88.50:40656,7c459f88962a4d07d7ccd6d0c94f891bb7a7ada0@65.109.26.21:13656,0108df8793ec07fa82ea202d54b70c603b827ea4@5.9.81.251:60656,70a02b29719f2a3f7347e03aac2681af6c634f33@158.220.100.181:40656,5397cc4860c38109d94bb56e21e0a13002cbe0e6@128.140.83.145:46656,85b2aa36f9df4d143311fa18745992d5cdd1d0d2@195.2.74.112:40656,e1b25355c160820148744c91d7ec79fea69b18bf@185.144.99.73:26656,dd82f0b844645b2047fa1b5a54f7fe575e80a134@188.34.167.232:26656,4d39946f5016ab24c7a62b251161dd7b1c043083@94.249.192.126:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
