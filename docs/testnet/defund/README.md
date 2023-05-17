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
* grpc: defund-testnet.grpc.kjnodes.com:14090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:14056
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:14059
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (10)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14056,6406dc6dff130a009ad79bb04eb29b731414811f@141.95.145.41:27656,e1b25355c160820148744c91d7ec79fea69b18bf@185.144.99.73:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@146.59.47.207:26836,ba0abf77c2dec230a7ae06b32d1abf63dbd48642@5.9.82.120:60656,6999cca6c55576a48d4f227b87dc904fbdb085aa@65.21.134.202:26576,6448d127ec3b31a1565603409c327699ff9c0b52@77.91.78.222:26656,7c459f88962a4d07d7ccd6d0c94f891bb7a7ada0@65.109.26.21:13656,4515f69283a8f3db159d35e72edce0ea0ddb6f1b@38.242.142.134:28656,8637f94f5cc834d34244a087e370c2ec9b2590bd@75.119.132.90:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
