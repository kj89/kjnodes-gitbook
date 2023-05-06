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
peers="7c459f88962a4d07d7ccd6d0c94f891bb7a7ada0@65.109.26.21:13656,ed9d651a48968b4c3c8e8f01e15dbb451eed195a@5.75.138.108:26656,6406dc6dff130a009ad79bb04eb29b731414811f@141.95.145.41:27656,6999cca6c55576a48d4f227b87dc904fbdb085aa@65.21.134.202:26576,4b740c782cc4e6561de519fffb23499f0541e84d@89.116.29.202:18656,4515f69283a8f3db159d35e72edce0ea0ddb6f1b@38.242.142.134:28656,5a93bbc7e9dc368ccadd2627b35364e0bf06035e@31.187.74.29:26656,8637f94f5cc834d34244a087e370c2ec9b2590bd@75.119.132.90:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14056,c24e38e2bf28f81a6935110c07cdeb95f5765ed1@65.109.84.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
