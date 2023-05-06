# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/dymension.png" alt=""><figcaption></figcaption></figure>

Dymension is a network of modular blockchains called RollApps  and at the center of it all is the Dymension Hub. Dymension  allows anyone to build and deploy their own consensus-free blockchain, a RollApp.

**Chain ID**: 35-C | **Latest Version Tag**: v0.2.0-beta | **Wasm**: OFF

[Website](https://dymension.xyz/) | [Discord](https://discord.gg/dymension) | [Twitter](https://twitter.com/dymensionXYZ)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/dymension-testnet](https://explorer.kjnodes.com/dymension-testnet)

## Public endpoints

* api: [https://dymension-testnet.api.kjnodes.com](https://dymension-testnet.api.kjnodes.com)
* rpc: [https://dymension-testnet.rpc.kjnodes.com](https://dymension-testnet.rpc.kjnodes.com)
* grpc: dymension-testnet.grpc.kjnodes.com:14690

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@dymension-testnet.rpc.kjnodes.com:14656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@dymension-testnet.rpc.kjnodes.com:14659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/dymension-testnet/addrbook.json > $HOME/.dymension/config/addrbook.json
```

**live-peers** (11)
```bash
peers="96ffe4b68c3f97cbeae4b4362634bf1054c7aeeb@142.132.151.99:15658,55f233c7c4bea21a47d266921ca5fce657f3adf7@168.119.240.200:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14656,8c3d6e4d065c6c171e2620f8ed8be5404fa61923@162.55.1.176:26656,7bbce7809296bf484ffcef6235550e03770cf81b@5.9.147.20:26656,5dbbb68e0c8a86bdc372cf1de0691f1cdc6a96ad@82.208.23.223:27656,e4dec3315020ac14bc82e6f4b0696d1b0f65d999@138.201.204.5:40656,8a66c13470c05acbd4d8711d21adbb67cc03dd1f@45.151.123.238:26656,4d2ec1e61d61550fc5bfacc57e971ff9b6181152@135.181.180.29:26656,4e94581e03f46c2bda293fa47db05c2fa8883256@190.102.106.50:29656,d982fab5b4befca7b162d24a74b9f95148dcdb01@5.231.205.142:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.dymension/config/config.toml
```
