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
peers="cf94df3ec5c7eca271a1d59b335ae743b2e0307d@185.215.167.45:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,e73a8c70a1e55c4ee14874c659a9084773ea56ed@95.217.104.49:36656,9f2087a5e238188451f515a8fc761c201167e2c7@65.21.245.170:26456,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,f31bb89bdb7c2d7867872f9fbbdda3d3d6a9a609@5.78.44.148:26456,6406dc6dff130a009ad79bb04eb29b731414811f@141.95.145.41:27656,e3c348467a8c88c0f65e2ca8a71875d2a384b8b4@185.16.39.19:60656,dd82f0b844645b2047fa1b5a54f7fe575e80a134@188.34.167.232:26656,c66d4d22039ad8afc8cc3cc873c69e2ddc37e70f@185.155.97.74:26656,94d95a32eff4f527fdf222550973a6ca8fa3eda6@217.79.187.110:40656,2b76e96658f5e5a5130bc96d63f016073579b72d@51.91.215.40:45656,49fd58f2953cbd87681bb2bb50ffaf176d5dcb50@65.21.57.72:26656,03f305b8efa44ed1520e73656029aeb144312505@94.231.131.216:26656,0eb9422efedd714d3db57d1ddfaad75f80a60518@5.161.99.35:26656,81985df787cb44c892b94395c18655238accce29@65.21.184.173:26656,55ab73ef10e4b6e6c98564df29565829cf12673a@65.108.159.127:26656,5afcb5884900d343384c9fb717d3104ab28ee200@162.55.175.251:26656,1fe1a13d22301e4a9d8f20d292caf2b178eb7c6c@93.183.211.209:26656,6999cca6c55576a48d4f227b87dc904fbdb085aa@65.21.134.202:26576,2f2aa0c7f3bb18836a51cc8dc4c6a26e17acd4c3@65.108.11.234:21656,ef08b9e04d26c13447ef1bc965f0e1f8943d4070@95.171.21.44:26656,1a4f0f016ffc8f6814835dc20f5bb7050b2eac90@38.242.239.25:26656,06c0fe8a5df43f71e88eaa3c07891338026ade9b@193.34.217.164:26656,4f1d96f5b8adb5bcdd59e61cb6e387ff12422a41@65.109.63.110:13656,4164f53d2b618419944312945cca1851d69738f5@185.177.116.41:26656,b8f0bee92d7b87ec4b9abf15888fefb6d2e07092@142.44.143.93:24656,4598cef0683d229c628702180959721eba8c598b@142.132.253.112:18656,875c807628a014aff8b4cdcbd812f183a0338d42@91.107.204.206:26656,6b94a3f12d8e694c3a735078e0cfa2b27940012a@95.214.55.62:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
