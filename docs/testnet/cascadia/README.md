# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/cascadia.png" alt=""><figcaption></figcaption></figure>

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
peers="001933f36a6ec7c45b3c4cef073d0372daa5344d@194.163.155.84:49656,f78611ffa950efd9ddb4ed8f7bd8327c289ba377@65.109.108.150:46656,783a3f911d98ad2eee043721a2cf47a253f58ea1@65.108.108.52:33656,6c25f7075eddb697cb55a53a73e2f686d58b3f76@161.97.128.243:27656,8757ec250851234487f04466adacd3b1d37375f2@65.108.206.118:61556,df3cd1c84b2caa56f044ac19cf0267a44f2e87da@51.79.27.11:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:55656,f075e82ca89acfbbd8ef845c95bd3d50574904f5@159.69.110.238:36656,63cf1e7583eabf365856027815bc1491f2bc7939@65.108.2.41:60556,d5ba7a2288ed176ae2e73d9ae3c0edffec3caed5@65.21.134.202:16756"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
