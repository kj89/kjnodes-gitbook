# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.7.0 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/lava-testnet](https://explorer.kjnodes.com/lava-testnet)

## Public endpoints

* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)
* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* grpc: lava-testnet.grpc.kjnodes.com:44090

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

**live-peers** (41)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,ed780f77754e8c4657b145144f0f95225d43bb03@65.108.224.156:27656,d1730b774b7c1d52dd9f6ae874a56de958aa147e@65.109.15.19:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,22c51515eea1df09dc872dc8843efb7fc73770b1@199.175.98.102:26656,c36a4007590af64d3e0a6b4736812ca6f6219561@65.108.9.164:23556,bfe21dd5af98aa42d213cd5bd943162a36b0505f@92.243.165.98:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,5676c8606f23471e220f8bf7317498a61bb93194@65.21.134.202:26686,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,397056c8cd7e2fce451d4f8e34ef24c0c9ffacba@176.9.44.113:26676,6a390c192797c62837030ad9058d4be672db4a0e@154.12.245.38:26656,74a979f0df53ef6f2ba9ab77c0c9fc5ba9c2bdc5@213.239.215.59:29456,9d5802ec3e10fbac150850ffdfa50f324e804b95@95.214.55.62:35656,95c59c9236f2e1c1c9ee35c6a9cd1b9f2fdc362e@213.239.215.115:29956,79fc521d683984e166526e74f88296599baf38c3@5.189.189.235:26656,a7944b8f0953e703d301670a9aa5312f3edf8cf4@65.109.106.91:24656,bb8c8cea499a1fa7e97922b5a9882c2360c6575a@176.103.222.21:26656,0a78dd75926983ba06de451480673487ffa1bcc1@199.175.98.106:26656,ae6b1f787fb2ba8e0bc9f180f9f7ee0453a53c71@23.121.249.57:26656,b591ef22e0c2082eb76dcac5ead95be55d01b695@65.109.178.147:26656,10c4405d04b2a221959de97f69c9a6258676f55d@161.97.79.100:26656,b7274e1274815e898fd52e4724c934820571fb5e@142.132.191.94:16656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,b12e2cb7eb121339eb5040dac618ba11763a10ac@91.107.195.107:26656,dfa93668152cb6b3a822c987f9c22110a1c2f314@178.18.255.221:26656,641426069e0de5daa02877db8c1d6854d7f59464@31.220.72.179:26656,0adbe1e790b58d19cc53a9839059a95d7d5d7aba@65.109.70.23:19956,91c02af6333972f222570a73f51feccda8a3ccf1@65.109.93.58:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,4e96723af8feb8a515573a7b9391e7bf7d562480@194.163.162.155:26656,0edd924d5422ab3cbf71d212c4e5511e622ee464@31.220.87.123:26656,35f045092f9c51ab743eec194438b91ecf8ce69e@65.109.116.22:11134,6641a193a7004447c1b49b8ffb37a90682ce0fb9@65.108.78.116:13656,c13b120d588c86008dc4ea5e3633b93c01831124@80.79.5.171:31656,66be93bd38fadeedde32f6adce6859b9700b1f11@182.217.153.83:26656,ab924e7944c332bd1b52c8733e262bbdd33cb5ac@116.202.165.53:26656,a2afdc48785be73f208af349e78d632b5556cc01@5.75.226.151:26656,6b7bfa6f0297b231f40a9284d45282af93320315@65.109.116.50:28656,fcd5a8f4aebc4c7100573914b7974a35cd389963@5.9.69.253:20656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
