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
peers="1d61222b7b8e180aacebfd57fbd2d8ab95ebdc4c@65.109.93.152:35656,f78611ffa950efd9ddb4ed8f7bd8327c289ba377@65.109.108.150:46656,2226b7ea3b32ef5cb0bae1162c2bd9d61da03236@87.117.38.192:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:55656,b71287a85b70df75e1405c6831634738e6b957ab@65.108.72.253:15656,f03ec36f6ca002ae13376248fc561dd394c8fe92@65.21.202.94:39656,2fb0a8dd1c16b363d779229ab009479e0e60b7c1@95.129.57.179:36656,893b6d4be8b527b0eb1ab4c1b2f0128945f5b241@185.213.27.91:36656,001933f36a6ec7c45b3c4cef073d0372daa5344d@194.163.155.84:49656,b7931fd033272aadea46c13b8f4aee91309e8c81@65.109.48.181:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
