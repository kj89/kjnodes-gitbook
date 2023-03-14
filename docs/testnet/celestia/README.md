# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/celestia.png" width="150" alt=""><figcaption></figcaption></figure>

Celestia is a minimal blockchain that only orders and publishes transactions and  does not execute them. By decoupling the consensus and application execution layers,  Celestia modularizes the blockchain technology stack and unlocks new possibilities  for decentralized application builders.

**Chain ID**: blockspacerace-0 | **Latest Version Tag**: v0.12.0 | **Wasm**: OFF

[Website](https://celestia.org) | [Discord](https://discord.gg/celestiacommunity) | [Twitter](https://twitter.com/CelestiaOrg)




## Chain explorer
[https://explorer.kjnodes.com/celestia-testnet](https://explorer.kjnodes.com/celestia-testnet)

## Public endpoints

* api: [https://celestia-testnet.api.kjnodes.com](https://celestia-testnet.api.kjnodes.com)
* rpc: [https://celestia-testnet.rpc.kjnodes.com](https://celestia-testnet.rpc.kjnodes.com)
* grpc: [https://celestia-testnet.grpc.kjnodes.com](https://celestia-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@celestia-testnet.rpc.kjnodes.com:20656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@celestia-testnet.rpc.kjnodes.com:20659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/celestia-testnet/addrbook.json > $HOME/.celestia-app/config/addrbook.json
```

**live-peers** (20)
```bash
peers="902680d35e2c36ad924aa78b02eb192933d812a8@144.76.61.180:26656,a1e08e481992149d50cb74144602334e71fa3aa3@62.232.97.106:26656,2b9c71541bb54d13e887b9ec6ff88bf09ea4c4a3@138.197.134.254:26656,b9a59a4e1e521ff3bf651c20a17bbad61fdd443d@104.128.62.172:26656,29c8a82a0be59a2c6a5d6fb2ad0a2e1b4d09de0f@186.3.232.252:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,8ec3dfbfa971264d8cdd86352ffa7bf95d341254@168.119.64.90:26656,572cb08735d4572fe62b2fc8b9555c479d8e162f@65.108.137.217:26656,46d3f4a8341c4523f4cafc778075688022280973@95.217.113.104:26656,6fbb911f2d20d86a77ecb8b8e95f6e80cfb62548@144.76.236.211:26656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@46.4.53.94:30582,f05e6a065b772dda4c7c0cbed40894a8c43416c7@57.128.86.3:26656,ed878d106169c4ac694f571d78b99d8abfe29b33@149.102.130.59:26656,b1b42ed03d101f8d0225b9796bfc9b628a2418c7@104.248.129.29:26656,b820b229105de6beeca1ab9b5e2aae787cdf73b8@141.94.162.118:26656,5c464c8a7f4182492f3e0ab71f14c3f3a43b5f7b@176.9.157.38:26656,da5dd22ae25a061d92cd7979e8977c449712a19d@46.4.23.42:26656,d78275c79f81efc0eb357cec3ec35877efec4974@57.128.74.131:26656,d046e88879cf5f6299cfc87ec05038ea98ee3aa0@5.9.154.105:26656,ebf8c82dd6bc37aebcc38f5bff61593d9e3ca370@65.21.163.230:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
