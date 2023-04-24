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
peers="8ce117ee1dd2a0f34b64a6fd13806a43ca913241@213.202.208.49:26656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,1a4f0f016ffc8f6814835dc20f5bb7050b2eac90@38.242.239.25:26656,1f526dc91429dc7c98d5b0ceb49f84f64c11336e@65.108.243.55:40656,2e85746b14e83108c991ef0f9f55c291f5e7d6a9@88.198.18.24:13656,2151e36f7696b39147f995c5171805c4eae0788a@194.87.113.40:26656,70c35e37f399fe02d41823c97188a4e5911d5b17@38.242.217.231:26656,72b1ac46a6924e6cb39c086cfec8da7b61d93ff6@38.242.139.98:26656,bc934501cffc27940d96e7775b6b8ae5122604ab@185.185.80.195:28656,fb95f32da1b85cb4c1fa04c2e75b045352a5507f@5.104.108.71:26656,fb76c9e69a87c0ffb2bbcd2adaa29b8c59a9698a@195.74.86.11:26656,48920dc679562d2f116f0b89ac77796377cfb130@194.146.13.254:26656,fdaa740662d6367dbac4c7ca9178cca325d36e42@65.109.231.80:26656,73c4f0b46f8e6b013980ddb5196932b00b09106f@94.103.91.211:40656,4a291d4568feed44abbb2ccae573a65cfd5bed20@65.109.70.45:26656,2609c228430dbb4652a62d17c09187a6ee831bff@188.233.19.198:26656,a6d9edebbd8b1b4651ca3cf5242879f573492d0e@49.12.236.218:26656,2931b7010fbbef00c06fd200e26989d903c1a249@89.163.155.252:27656,445bebcbfc243bf78c3a2616bff0eedc5e4b6797@95.171.21.43:26656,beb10b655c17c4dd306c5afe51b5bcb81ff46e9c@195.128.158.119:26656,14393b49195fc9496191d5091e53c9c2f55da648@62.183.54.219:40656,492f8fbaf5270cf739941979593757bea7bc8549@116.202.241.157:10156,86caf6297ae00fb58b58a272984275c592b2fdf7@65.109.84.216:56656,7c459f88962a4d07d7ccd6d0c94f891bb7a7ada0@65.109.26.21:13656,4b740c782cc4e6561de519fffb23499f0541e84d@89.116.29.202:18656,e3c348467a8c88c0f65e2ca8a71875d2a384b8b4@185.16.39.19:60656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,34b72721aa503574a0709b1859fb1da2aa12ce70@88.99.3.158:11256,9fa1eb3779b039e0072e57aeed127b99e3d6062a@217.79.187.22:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
