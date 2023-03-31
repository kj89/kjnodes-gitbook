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
peers="83e19abc0a16b1a639b6f77e19ecca33c5971452@65.109.171.250:56656,78c53aca778b1239158cf4bf6a3aeeb2239501bb@38.242.216.35:40656,74e6425e7ec76e6eaef92643b6181c42d5b8a3b8@65.108.231.124:18656,e73a8c70a1e55c4ee14874c659a9084773ea56ed@95.217.104.49:36656,c9756dd10dd5166bb8ae74aa7f7e51bc1869bf95@84.54.147.241:28656,7e266e8c84366e1fbf0a82efba306ef46214455d@38.242.226.162:40656,1962eafeec4fc49af6f9bc407a5dd7723ac22e8d@172.174.23.55:26656,343756674fbe6a2dfed5a455bb9ad24f02ec5bf0@38.242.244.176:26656,b2dab4e2f5e9ebf9901e9e8bf817af36c705b458@65.109.131.246:26456,6ae6e82fe96e9386e40050958f2f3722cdad9826@178.205.12.0:26656,c806a2e792811afb419c9ff8edd793369c722394@135.181.28.80:26656,d2c54bc142fdd6f033c967699e2cd604925551ad@95.171.21.42:26656,e3c348467a8c88c0f65e2ca8a71875d2a384b8b4@185.16.39.19:60656,14d989a7ff26fd1aba1349497bb9ab0f8ed5c078@109.123.254.14:26656,b8f0bee92d7b87ec4b9abf15888fefb6d2e07092@142.44.143.93:24656,0108df8793ec07fa82ea202d54b70c603b827ea4@5.9.81.251:60656,b9110b9df51b2d0e66537c43138a7b4ace26ff71@154.53.51.114:30656,64db984bc93ab23b3a1e2d8f060b56f1ef596b51@178.124.209.101:26656,5a173cbd537b8f75063b2db51131fa906236376e@65.109.93.152:32656,ca3e78c3681a8a0445a8c5ae0da07f238d221ef4@37.27.0.96:26656,f5cd4e7dcc01f8b0343474f35b01137126097a58@80.85.139.232:26656,608491d7226330037bc194c37cca8cc2d50f391c@207.180.241.114:40656,78258c1cfbd7a78da1417b22700dc790912299eb@89.163.225.39:26656,8b7c1f3b34001f906175e4e187ddf096db469042@194.163.143.176:26656,2a2e46081bc82ac711df8e54159004440de6bcc4@65.109.116.50:33656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
