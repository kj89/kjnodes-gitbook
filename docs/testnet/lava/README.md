# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.4.3 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)


## Public endpoints

* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@lava-testnet.rpc.kjnodes.com:44656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@lava-testnet.rpc.kjnodes.com:44659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/lava-testnet/addrbook.json > $HOME/.lava/config/addrbook.json
```

**live-peers** (19)
```bash
peers="e8256f9fedf27b6de76c8a13e2db050d0a7bd905@95.216.42.83:26656,2ec5dc5b90e6c200cbfd4b53c90c0c5d55c33914@139.59.189.24:26656,8ef9baeaaf8e4e3c478c74b2334ab61d7190be72@91.144.158.116:46656,c506970f0ac6e99ba3e1e01da33a39315c8b7aa1@38.242.141.94:26656,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,1884699b139f95c2e38c75380493c68f72ffedb0@86.48.1.143:26656,6d370f3301a19cd4d1788172d8d1dbfd506eac4e@89.252.21.37:26656,ebcdfc1eb6706d364701936281b29f41cc073394@65.109.38.218:26656,5f04e56cabc20ab2e94b03022f024a310dfdf840@85.10.198.169:11656,f35a72a6ddf4e5cd045121b177ee54759e68163d@167.86.112.109:26656,88023a76785c2f1d7a3d6ce2c48713c5ba94e47b@65.109.82.249:36656,2cb465a7c919321978f89701b4ae07ac505f7ad8@194.163.184.228:26656,a724b94c593241890022e204e0065d8baa67168c@116.202.227.117:44656,8cd81b9119e4aa45fe549dd12543de862457c989@38.242.155.47:26656,acc3fe0b067e10b55c060b2f740d6193bf15a315@15.204.207.179:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,377370216f2c003b9d00118ec5373ed21f13aab3@185.16.39.19:35656,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
