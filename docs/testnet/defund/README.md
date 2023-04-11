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

**live-peers** (26)
```bash
peers="86caf6297ae00fb58b58a272984275c592b2fdf7@65.109.84.216:56656,4a291d4568feed44abbb2ccae573a65cfd5bed20@65.109.70.45:26656,1e79c5a5da82a33cfb507089c028480ec455f24d@145.239.143.76:10256,d9975542e05f25e92ece8e8ca60f3f0b9af3315f@135.181.37.97:26656,e73a8c70a1e55c4ee14874c659a9084773ea56ed@95.217.104.49:36656,64c045f78cf1c126e2e2da4837a4f3b91a14bb65@154.26.128.79:40656,8be5a026d01450c07f89ff2281a15b0862070be8@94.181.173.92:26656,aabae0bb071b20c73f335c3c036ab119a851d175@217.76.62.24:26656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,694339f20806dd0b346dc9a25ff9947507735006@116.202.161.165:29656,ffb2898494cdbd6625d962ea4511c29507177c62@164.68.103.176:26656,7b837ce6cdb7964625fb70844d59de744573bc9f@65.21.136.154:13656,da77231e4a499106b2fa2f0d64e553c2a9e2203b@65.108.199.206:28656,3f2b1ce13248281f25712c2b69fde573c5d8effb@178.207.108.79:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,fc8ad183d32ca52eabc2d3af8e1e85b06ca1286a@159.89.117.7:26656,40cc05a9fc2aa1d1cab32b552ca10c94adc215f4@95.217.105.41:13656,102b26ff4ad6fadedd28f047e408174a6f07e6eb@77.120.110.229:40656,0eb9422efedd714d3db57d1ddfaad75f80a60518@5.161.99.35:26656,fea7d3dc17276666cd03907e1c2446dd5a89c1af@94.190.90.38:31656,eb7040eb80f3a0b62df828d38d818b3aec554b50@38.242.237.125:26456,8f33fb0dcc71c094a87bb94db0b5d5e1a4d23a84@82.208.23.192:26656,a45329c77b1047a6e9cec925f5974daf5f78e36c@95.217.119.251:13656,4b740c782cc4e6561de519fffb23499f0541e84d@89.116.29.202:18656,dcf01e91fb6ccafeffe24bd3bd683a30a4907a98@144.126.138.62:30656,2788c4e5178166010baf8786ad3091a9fcc1a730@5.78.101.216:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
