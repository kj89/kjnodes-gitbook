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
peers="14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,5ab0449599aabcf90f664003c2ef1510ecd33b1b@65.21.203.204:11656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,9057ee9d3d9b3c42c184dc89a7b2a07026b81a45@31.220.76.131:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,9d5802ec3e10fbac150850ffdfa50f324e804b95@95.214.55.62:35656,a2afdc48785be73f208af349e78d632b5556cc01@5.75.226.151:26656,e4ebf07ed08ff8ee26a9a903d63ad34d1f59393e@95.217.35.186:56656,e77870b8732c952f40813e4e622cc2f108fd0223@154.53.55.153:26656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,22bd49cb251e649816d2cb6f24897dd2b4602dc4@149.102.157.34:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,ec8065014ed4814b12c884ed528b96f281104528@65.21.131.215:26686,b7274e1274815e898fd52e4724c934820571fb5e@142.132.191.94:16656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,c19965fe8a1ea3391d61d09cf589bca0781d29fd@162.19.217.52:26656,013f0163d37428ed99eacd8ee84059da5c243981@5.161.132.217:26656,beaedffb147f5908523589c212c971c292fef46c@65.108.226.101:28656,f68c57ca955420779773f9320a6b7710c2b29f73@188.191.36.222:26656,35f045092f9c51ab743eec194438b91ecf8ce69e@65.109.116.22:11134,0a78dd75926983ba06de451480673487ffa1bcc1@199.175.98.106:26656,799077b3a3b52094ab3ca19b6a7ecab89c50cb61@185.144.99.97:26657,8a20f8f798c5073f0867812e691f54b5cd0dd65d@109.123.242.188:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,6641a193a7004447c1b49b8ffb37a90682ce0fb9@65.108.78.116:13656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,53cba364b17674a182a19bd0fd6fc06ffae488b0@161.97.133.186:26656,0d6983bcd192c0b4a0f61e6d849c152704e2f017@91.107.148.5:26656,0728346503162452713574f36a1eb964d0b433a8@144.126.138.81:26656,1ec38451f3e45535ceba905d1442310c69aaf93e@217.76.61.37:26656,a7944b8f0953e703d301670a9aa5312f3edf8cf4@65.109.106.91:24656,4fc42fdf634ef542094c7a44f22e031acea61162@91.77.165.172:27656,c4e5e9a731eeaf8d138481c70546b9c34dd3e23e@213.136.92.28:26656,cb722cc36541920d3907cd67743db5444f53e80b@95.70.184.178:24656,4e96723af8feb8a515573a7b9391e7bf7d562480@194.163.162.155:26656,ac99b8d7f3d863baa09cf6378057b78c4f02d029@91.233.173.45:26656,6b7bfa6f0297b231f40a9284d45282af93320315@65.109.116.50:28656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:19956,31550f0ec97d7148b2dae0de2a02240f88d1cfcf@85.114.134.219:12656,c13b120d588c86008dc4ea5e3633b93c01831124@80.79.5.171:31656,ab924e7944c332bd1b52c8733e262bbdd33cb5ac@116.202.165.53:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
