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

**live-peers** (27)
```bash
peers="74e6425e7ec76e6eaef92643b6181c42d5b8a3b8@65.108.231.124:18656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,6ae6e82fe96e9386e40050958f2f3722cdad9826@178.205.12.0:26656,cf94df3ec5c7eca271a1d59b335ae743b2e0307d@185.215.167.45:26656,e73a8c70a1e55c4ee14874c659a9084773ea56ed@95.217.104.49:36656,f31bb89bdb7c2d7867872f9fbbdda3d3d6a9a609@5.78.44.148:26456,e3c348467a8c88c0f65e2ca8a71875d2a384b8b4@185.16.39.19:60656,6b9797483562f7836e0ab23e63b911daf324b55d@65.108.238.147:28656,1a4f0f016ffc8f6814835dc20f5bb7050b2eac90@38.242.239.25:26656,b4a55ed44fbfdd8cc29c893a306210d54772cb70@74.235.61.189:26656,946853034fa6ca41edbf7293aeb79d05f8248c78@91.189.129.20:26656,338858c463b518d6eca7a7c3bd404e33b796b074@89.163.155.117:40656,738dd4cf6cb4e60b2976b9b82d1787b8f8d9ae73@45.132.106.203:26656,e332f554fab24feff380b906813a1d9759c6ceeb@167.235.10.164:13656,878c7b70a38f041d49928dc02418619f85eecbf6@65.109.18.166:45656,335ef25c13bc47350135710e2e056adf4d277c8f@116.202.227.117:40656,a56c51d7a130f33ffa2965a60bee938e7a60c01f@142.132.158.4:10656,806568109c80f3c52901f7f96e412a668a36afa0@185.107.237.145:26656,8517cda53e2cf38197e02b93e6e6a441645ad92d@89.223.53.232:36656,da77231e4a499106b2fa2f0d64e553c2a9e2203b@65.108.199.206:28656,a4996d4a22f2caac032f2b775d81ec238a239c37@94.130.200.205:26656,7dff00a6d6678dd1f29df92774bb15cda17fff28@185.92.149.140:26656,e82f23c5bc0122d14bc63d8d4248140a7838ab52@77.242.105.144:26656,17db2eb88b0f63999593ce5b8206a46c0ab35436@46.8.220.81:26656,d7e78e8abdb68321b8f1f9dc40b0636908b81cf7@65.109.128.79:26656,88668b1252b6a1fe449f3d26ea8e761e75091863@154.53.55.91:30656,3209ec925afead6706ac250aae88d1b85a45a2d3@167.86.85.247:30656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
