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

**live-peers** (10)
```bash
peers="42ec68fe0eeeff1bb0ef64e1ae74c99c8d58c293@78.46.106.75:15656,001933f36a6ec7c45b3c4cef073d0372daa5344d@194.163.155.84:49656,eb3a413b8a2baf1f544d4129572919257d5db53b@65.109.82.112:28656,035df68157b66066b00390d74c6d4f4895cb1ef9@95.217.155.184:26656,565899a1b074310c8e7acb9924fbe65cb04c8e33@185.229.119.8:26656,bdb5c5533afc747813da104d5a940292ac4fb071@195.2.75.84:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15556,ed0bf599702c33b800d2bc16f7968c03a678406d@65.109.50.234:26656,8a0e76b9cdfe2e80bca2e9ea270d57af17cfaf06@65.108.146.240:18656,b3646894ea4aef0244f5256a202cc8362d91de8e@109.123.245.20:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
