# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-3 | **Latest Version Tag**: v0.2.1 | **Wasm**: OFF

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)


## Public endpoints

* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)

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

**live-peers** (11)
```bash
peers="0484eab6881ba458c5988296403963aaf273700b@157.90.236.25:18656,58d46050cf77065d27e9526a7e93c8f814cc036a@194.146.13.185:26656,9cbaf117258ac247bce37f314d1a2ddba34b5ad6@194.163.190.54:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,35b9a1c3c7a597413f4c999a9fc1e6cb0cc8b978@65.108.100.53:36656,b32e6619a1c7998519d2d38828e34ace7b773852@65.109.84.250:36656,c34b4bc09946950d3fb8059d4954f45ed24e25bc@89.163.255.100:26656,34caa18dc803a7c1c5da380f85f18bbf6e2e6126@162.55.33.123:26656,a713c7dbfbcf0704f591bcc07d1f116303c44b27@45.87.0.238:26656,f5c51a2c40257da4524776717f91590ccad593ec@176.124.221.134:26656,5e6354412f3742ac76e37838236707b373c1de43@185.250.37.162:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
