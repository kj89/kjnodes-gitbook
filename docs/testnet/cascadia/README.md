# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cascadia.png" width="150" alt=""><figcaption></figcaption></figure>

Cascadia is a layer-1 blockchain built to explore the  nature of incentives on network effects, starting  with ve-tokenomics.

**Chain ID**: cascadia_6102-1 | **Latest Version Tag**: v0.1.1 | **Wasm**: OFF

[Website](https://www.cascadia.foundation) | [Discord](https://discord.gg/cascadia) | [Twitter](https://twitter.com/CascadiaSystems)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/cascadia-testnet](https://explorer.kjnodes.com/cascadia-testnet)

## Public endpoints

* api: [https://cascadia-testnet.api.kjnodes.com](https://cascadia-testnet.api.kjnodes.com)
* rpc: [https://cascadia-testnet.rpc.kjnodes.com](https://cascadia-testnet.rpc.kjnodes.com)
* grpc: cascadia-testnet.grpc.kjnodes.com:55090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@cascadia-testnet.rpc.kjnodes.com:55656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@cascadia-testnet.rpc.kjnodes.com:55659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/cascadia-testnet/addrbook.json > $HOME/.cascadiad/config/addrbook.json
```

**live-peers** (10)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:55656,796a6a0960d7366123f3a829ad917ae0a4f7e09d@91.223.3.190:55796,5623331ab53459146cbb60efadf42899373f844b@37.27.6.70:26656,603f78beb8ddc84de1f6375a792a9042f4e255c5@37.27.10.160:26656,e6e3fbc13c1903ac758ce7c6fa180312b89af2e8@142.132.248.253:25656,f075e82ca89acfbbd8ef845c95bd3d50574904f5@159.69.110.238:36656,001933f36a6ec7c45b3c4cef073d0372daa5344d@194.163.155.84:49656,d5ba7a2288ed176ae2e73d9ae3c0edffec3caed5@65.21.134.202:16756,c9256e4f42a23bbdc9ea79805f497a1923a4beac@65.108.230.113:17096,ba401f52e3ecad90d0d8e8f69f4aba41a0ffa09d@34.83.82.43:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
