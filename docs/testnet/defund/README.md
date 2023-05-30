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
peers="c1c6cf5859c43fb3acd19ccdb78a4caa0a151ff7@45.85.249.107:27656,f417252166d6508a75371573f3c12e8abca238a5@65.108.108.52:13656,a79130668102f116a23cfcf9fd94623de4a223fe@81.30.157.35:10656,5c2a752c9b1952dbed075c56c600c3a79b58c395@146.59.47.207:26836,4515f69283a8f3db159d35e72edce0ea0ddb6f1b@38.242.142.134:28656,9f8ad11f0fcdd0bbbbbd4fcf54dbcd5e44db041d@109.123.243.13:27656,035ff6d94b5c62d1830d71b25c259e11a679250d@38.242.158.116:27656,bc934501cffc27940d96e7775b6b8ae5122604ab@185.185.80.195:28656,7a3c4079964eaca46f63f9a4ba37997ae55bee60@45.85.249.93:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
