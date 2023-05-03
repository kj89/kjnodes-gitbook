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
peers="5a93bbc7e9dc368ccadd2627b35364e0bf06035e@31.187.74.29:26656,ed9d651a48968b4c3c8e8f01e15dbb451eed195a@5.75.138.108:26656,34b72721aa503574a0709b1859fb1da2aa12ce70@88.99.3.158:11256,6406dc6dff130a009ad79bb04eb29b731414811f@141.95.145.41:27656,4b740c782cc4e6561de519fffb23499f0541e84d@89.116.29.202:18656,0108df8793ec07fa82ea202d54b70c603b827ea4@5.9.81.251:60656,251c53c762273adbb7853569d17af2a6f00e9c7a@65.108.101.124:13656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14056,a6d9edebbd8b1b4651ca3cf5242879f573492d0e@49.12.236.218:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
