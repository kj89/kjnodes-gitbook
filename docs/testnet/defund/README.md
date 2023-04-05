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

**live-peers** (25)
```bash
peers="74e6425e7ec76e6eaef92643b6181c42d5b8a3b8@65.108.231.124:18656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,e73a8c70a1e55c4ee14874c659a9084773ea56ed@95.217.104.49:36656,34643d937e70f0887edbbeb160517ecc70aaad1a@86.48.5.250:26656,e332f554fab24feff380b906813a1d9759c6ceeb@167.235.10.164:13656,bccd2003a7eb23008479c76427ac2c276160e09a@75.119.154.72:26656,6807702de3ce32c4b26155f5ca26d3085704819c@20.124.182.98:26656,dcf01e91fb6ccafeffe24bd3bd683a30a4907a98@144.126.138.62:30656,2218acbe81b1f57da84cf0db5ebb6fe65e5e3362@65.21.205.248:18656,6f2a7f58d0fd205582445d2113c419f91b42dd4a@86.48.25.249:26656,b4a55ed44fbfdd8cc29c893a306210d54772cb70@74.235.61.189:26656,4275e0c66c6aceb36ada91f2fcbaed80cc9b7a51@95.111.241.122:30656,c9ea68a2fbb8d304eda0dd3d453f395a14a1bc1e@94.130.55.152:26656,e3c348467a8c88c0f65e2ca8a71875d2a384b8b4@185.16.39.19:60656,d033e63be16b3a31d29f98541d79a39f05459e67@185.208.206.74:26656,7b1c0b4e181d3740cbc81169ef7781cf600aa4c3@144.126.157.206:30656,f31bb89bdb7c2d7867872f9fbbdda3d3d6a9a609@5.78.44.148:26456,cf94df3ec5c7eca271a1d59b335ae743b2e0307d@185.215.167.45:26656,278602404e78c23f5aff7a04802179ad7ffaa676@18.234.102.132:26656,1f3d2207563de47996cf3f4cb14ab300b249ba95@194.146.13.180:26656,bfef03639bddf4fa503bb75c83af2b5f12c8276c@161.97.155.154:26656,6ae6e82fe96e9386e40050958f2f3722cdad9826@178.205.12.0:26656,c584a5f8c28c7548752fdfea6cf2942d5e10c82e@188.34.178.190:56656,7c459f88962a4d07d7ccd6d0c94f891bb7a7ada0@65.109.26.21:13656,f858f9b2a09dedcb784c5ad9b5042d258822c3e0@154.53.54.154:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
