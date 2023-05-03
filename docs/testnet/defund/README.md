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

**live-peers** (9)
```bash
peers="4b740c782cc4e6561de519fffb23499f0541e84d@89.116.29.202:18656,6448d127ec3b31a1565603409c327699ff9c0b52@77.91.78.222:26656,7d51a0519639c75d7a33f7ebe22319b1ef9eb9ad@185.209.230.89:26656,0eb9422efedd714d3db57d1ddfaad75f80a60518@5.161.99.35:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14056,5a173cbd537b8f75063b2db51131fa906236376e@65.109.93.152:32656,bda598af0c96d72a85c3b6840138d929b8c4e762@84.46.248.207:26656,8a650a9761db8abc1096abc3d4a68431600ae835@62.171.149.101:46656,424b76ff5aadcc5a58debf8e02ca251c2e521050@168.119.165.240:26456"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
