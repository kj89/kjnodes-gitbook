# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cascadia.png" alt=""><figcaption></figcaption></figure>

Cascadia is a layer-1 blockchain built to explore the  nature of incentives on network effects, starting  with ve-tokenomics.

**Chain ID**: cascadia_6102-1 | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://www.cascadia.foundation) | [Discord](https://discord.gg/cascadia) | [Twitter](https://twitter.com/CascadiaSystems)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cascadia-testnet](https://explorer.kjnodes.com/cascadia-testnet)

## Public endpoints

* api: [https://cascadia-testnet.api.kjnodes.com](https://cascadia-testnet.api.kjnodes.com)
* rpc: [https://cascadia-testnet.rpc.kjnodes.com](https://cascadia-testnet.rpc.kjnodes.com)
* grpc: cascadia-testnet.grpc.kjnodes.com:15590

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@cascadia-testnet.rpc.kjnodes.com:15556
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@cascadia-testnet.rpc.kjnodes.com:15559
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cascadia-testnet/addrbook.json > $HOME/.cascadiad/config/addrbook.json
```

**live-peers** (11)
```bash
peers="e6e3fbc13c1903ac758ce7c6fa180312b89af2e8@142.132.248.253:25656,624b1a13e77bd9f3cde44f4ed6a32eff1a95611b@195.201.59.194:26156,32bcc51674dd83a316323a67918c1cee25163291@65.109.72.12:26656,1168af52cf36c68e2405b3041c8d53ed1ca169be@65.109.158.190:26656,4ead67f38f3163a5c849333faaaf760b6d9eda8e@185.237.253.88:26656,e500ca28e37c1fcd7f7167a6fa35c90e8d0a78f5@185.182.184.191:26656,d3e1ce95ac1e2830296eff1c952b89d6c3d84f7a@217.197.117.53:61256,40739dda0aa1fd152faecfd540ddb876481fa7b2@170.64.158.48:18656,df3cd1c84b2caa56f044ac19cf0267a44f2e87da@51.79.27.11:26656,4b1b5e4a8f3a0cbaf235b13e68184a2d9d376b2b@178.20.44.156:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
