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
peers="eb7040eb80f3a0b62df828d38d818b3aec554b50@38.242.237.125:26456,035ff6d94b5c62d1830d71b25c259e11a679250d@38.242.158.116:27656,274aa6457948bb8355dc8e5d3c2f7074fa699e39@37.27.7.187:26656,e0ab16d47276dee411fc01abc86c787d95ef6aba@65.109.111.204:29656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,f8036fa5e78f72606209d8022905a96364b82d19@185.209.230.110:27656,5ce286faea0eb730e6d4f3636ab572fea20a879d@86.48.5.92:27656,48920dc679562d2f116f0b89ac77796377cfb130@194.146.13.254:26656,ffb2898494cdbd6625d962ea4511c29507177c62@164.68.103.176:26656,9f8ad11f0fcdd0bbbbbd4fcf54dbcd5e44db041d@109.123.243.13:27656,354485ffcd96d2c292969fae86624f754924bb8c@91.77.165.172:28656,54315866e9a9c0bd7611a42a1caaf4a244316eb3@65.108.200.60:13656,e73a8c70a1e55c4ee14874c659a9084773ea56ed@95.217.104.49:36656,dfa7af21b8c6efebe8aa6028196324f9e0540bbc@94.130.55.76:39656,912d95a925bb827e1f6ac08810742d658fd2268e@185.218.126.186:27656,e494f017a60c9be7b73541ea9356affbeee1c9cb@178.18.247.73:27656,f417252166d6508a75371573f3c12e8abca238a5@65.108.108.52:13656,1a8e8d6667615f4836c1c1403563a26a1044fd00@116.203.158.189:26656,436a10ea3a057eb86a7a2e33208634b677a90de1@212.232.52.212:26656,d39e6d823cace974d0836b1bd9df415f54efbaf4@95.216.227.146:27656,35bd24cfb2d71f1091b082376e8eab870a0496a1@65.109.82.75:46656,7ea4373346eea6b2c4f77655883e915481609028@185.177.116.123:27656,4f1d96f5b8adb5bcdd59e61cb6e387ff12422a41@65.109.63.110:13656,9d93136c7e4af2de3f8bb6c82c5d1f0b30b7b657@38.242.225.217:27656,da77231e4a499106b2fa2f0d64e553c2a9e2203b@65.108.199.206:28656,0eb9422efedd714d3db57d1ddfaad75f80a60518@5.161.99.35:26656,127b4bca7027bd677d342eed279acbdbe52832c5@178.18.245.137:27656,790d14b181c9f538bfa81afaf70fe78c3e9b52e2@38.242.199.69:26656,bc934501cffc27940d96e7775b6b8ae5122604ab@185.185.80.195:28656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
