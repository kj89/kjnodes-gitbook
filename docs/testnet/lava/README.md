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

**live-peers** (39)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,dfa93668152cb6b3a822c987f9c22110a1c2f314@178.18.255.221:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,6ba3b6ec03839afffa64c83e18ff80a681f4968d@65.108.194.40:21756,11d25deba9c655a7312716810e3975fe175ada01@5.161.58.198:26656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,0e9062ed560ce78eba346f1d73ae3ca9eeea5985@142.132.248.253:24656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,b4d53b1e7a2fee2192a30e411ba83136c07ab595@161.97.147.107:26656,b12e2cb7eb121339eb5040dac618ba11763a10ac@91.107.195.107:26656,0a78dd75926983ba06de451480673487ffa1bcc1@199.175.98.106:26656,509eaf8341cca511c8a3127affaae2251593d514@161.97.148.146:56656,1377a4d43745a650fe21cc87641818854e9fbdcf@65.109.88.254:35656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,7ec0007e3c24012db9d5596745db5cb7c8321b50@95.216.7.169:60956,5ab0449599aabcf90f664003c2ef1510ecd33b1b@65.21.203.204:11656,0205350b2227d273d06bd70123c39752bdcc5ed4@207.180.203.195:26656,5a469a75fb05eddf2d79fb17063cc59e84d0821a@207.180.236.115:34656,75ed1e87b48d6e1ab341e3568708c9fb81743ffa@65.109.88.251:11036,9d5802ec3e10fbac150850ffdfa50f324e804b95@95.214.55.62:35656,d64aa8f4d864daac54639cd1fdebbf4c464ba4f1@5.75.235.206:26656,035d086cc418352aba9e679e079f17391791ccc6@178.208.252.54:27656,a7944b8f0953e703d301670a9aa5312f3edf8cf4@65.109.106.91:24656,e4ebf07ed08ff8ee26a9a903d63ad34d1f59393e@95.217.35.186:56656,149f9f017344ce9cebb637baa7cab57a28f3a8c3@86.111.48.159:26656,df06418afe0c3d6ebbe8cd233dc9bed02b87cc62@65.108.107.241:26656,641426069e0de5daa02877db8c1d6854d7f59464@31.220.72.179:26656,f9af0186eec9a88a5a657deb9a7deff34c05d99f@86.111.48.156:26656,bc2e99e6004bb0b87c72ca10f20cd1617edf70fe@141.94.73.93:56656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,0314d53cc790860fb51f36ac656a19789800ce5c@176.103.222.20:26656,4e96723af8feb8a515573a7b9391e7bf7d562480@194.163.162.155:26656,0df9cc98fd8e88920efd02425292813108e14a45@185.202.238.214:26656,35f9c3d2825b05a2aded66e9de66102507e6ca0f@207.180.210.152:26656,fa908ede438730a87c02e113a95aac206398706d@207.180.207.68:26656,11cde1d5d6da6818c2dd75b8ed4aee6d89616837@185.209.230.186:26656,8b774eabd1b4fbffdf9d14fba3d4a1690c69d0ad@65.109.24.227:30656,a2afdc48785be73f208af349e78d632b5556cc01@5.75.226.151:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
