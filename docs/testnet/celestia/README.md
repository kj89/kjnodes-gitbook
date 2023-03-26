# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/celestia.png" width="150" alt=""><figcaption></figcaption></figure>

Celestia is a minimal blockchain that only orders and publishes transactions and  does not execute them. By decoupling the consensus and application execution layers,  Celestia modularizes the blockchain technology stack and unlocks new possibilities  for decentralized application builders.

**Chain ID**: blockspacerace-0 | **Latest Version Tag**: v0.12.1 | **Wasm**: OFF

[Website](https://celestia.org) | [Discord](https://discord.gg/celestiacommunity) | [Twitter](https://twitter.com/CelestiaOrg)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/celestia-testnet](https://explorer.kjnodes.com/celestia-testnet)

## Public endpoints

* api: [https://celestia-testnet.api.kjnodes.com](https://celestia-testnet.api.kjnodes.com)
* rpc: [https://celestia-testnet.rpc.kjnodes.com](https://celestia-testnet.rpc.kjnodes.com)
* grpc: celestia-testnet.grpc.kjnodes.com:20090

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
peers="b766d36a1e3bcefc5e5befddfad7b4589ba28a21@162.55.242.83:26656,cc167c48a977160de9f9bbb5c3b80ddb7d585a67@176.9.156.135:26656,de36dc2bc32ecaacafb213d173f6218f93ebb306@144.76.105.14:26656,da5dd22ae25a061d92cd7979e8977c449712a19d@46.4.23.42:26656,02241bb63c01fb52033029f7155c3db5d7846c1f@168.119.64.26:26656,b1b42ed03d101f8d0225b9796bfc9b628a2418c7@104.248.129.29:26656,f05e6a065b772dda4c7c0cbed40894a8c43416c7@57.128.86.3:26656,6f3d14f3ca7bb06e6ba560ab78e70aa77c0ca0d0@65.108.99.238:26656,6df4a6d0db5a771b84055646fe3814c655dd3428@95.216.163.64:26656,a1e08e481992149d50cb74144602334e71fa3aa3@62.232.97.106:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:20656,6fbb911f2d20d86a77ecb8b8e95f6e80cfb62548@144.76.236.211:26656,a86db178fbf5f9072b1bd0df465b947c5bb715e1@142.165.207.19:46656,9fd9275b49d478bf8352dc160dc0e9a184011098@217.182.194.152:26656,29c8a82a0be59a2c6a5d6fb2ad0a2e1b4d09de0f@186.3.232.252:26656,dc76534dfede17c47ec162fce0937b446a627820@206.189.92.202:26656,7db3d8fa353b4cf293244f7526cdabfaebef53bf@158.160.24.133:26656,143a1eda55f71240a9b22a1bedc00868fd2a46de@65.109.19.168:26656,5d02fa37f0fe3f198b3fdcea78b8961d04425b5d@185.227.135.173:26656,2b9c71541bb54d13e887b9ec6ff88bf09ea4c4a3@138.197.134.254:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.celestia-app/config/config.toml
```
