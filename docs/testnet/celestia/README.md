# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/celestia.png" alt=""><figcaption></figcaption></figure>

Celestia is a minimal blockchain that only orders and publishes transactions and  does not execute them. By decoupling the consensus and application execution layers,  Celestia modularizes the blockchain technology stack and unlocks new possibilities  for decentralized application builders.

**Chain ID**: blockspacerace-0 | **Latest Version Tag**: v0.13.0 | **Wasm**: OFF

[Website](https://celestia.org) | [Discord](https://discord.gg/celestiacommunity) | [Twitter](https://twitter.com/CelestiaOrg)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/celestia-testnet](https://explorer.kjnodes.com/celestia-testnet)

## Public endpoints

* api: [https://celestia-testnet.api.kjnodes.com](https://celestia-testnet.api.kjnodes.com)
* rpc: [https://celestia-testnet.rpc.kjnodes.com](https://celestia-testnet.rpc.kjnodes.com)
* grpc: celestia-testnet.grpc.kjnodes.com:12090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@celestia-testnet.rpc.kjnodes.com:12056
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@celestia-testnet.rpc.kjnodes.com:12059
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/celestia-testnet/addrbook.json > $HOME/.celestia-app/config/addrbook.json
```

**live-peers** (14)
```bash
peers="3cf4a639196a73028136cd590c4682a80d41c460@3.125.129.136:26656,6c73374cb78a543e2dd3eb218c29386392da2cf5@35.210.99.77:26656,3e3d0887865ca6feaf7e99a50dbfb41e591a9781@141.94.138.48:26688,0196b56324c6fd3dd31110d3cb06dc169a1e1310@194.62.97.31:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:12056,8f14ec71e1d712c912c27485a169c2519628cfb6@185.225.232.196:21656,7a89c8c63ee0a305d236eabb435ea54f1c08d3dd@125.143.190.194:17002,62f6abc162db99389f13a1cdf1abaeb6efb647a7@35.210.78.75:26656,f6070ab2af725d4f62bb81dbd30dc2047bc66d04@65.108.193.249:2270,64a3c4a25abefdd2087da0d7cd1abafe8a354953@209.97.138.19:26656,7d6d1d1c3498687d4705fe4c7216623797835fae@74.118.136.164:26656,f7916ed6f294f94740b98b5a7f21d368589fee56@202.61.194.254:60956,b9a59a4e1e521ff3bf651c20a17bbad61fdd443d@104.128.62.172:26656,1f11577400a5caadedc01261e0f4902983445fb1@46.4.53.94:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
