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

**live-peers** (30)
```bash
peers="190d96828cdeba320b60f4704d2f35a404c97fda@65.109.92.230:15656,783a3f911d98ad2eee043721a2cf47a253f58ea1@65.108.108.52:33656,c6e3921222655345d8296353994e917f13a1b4a1@65.109.92.79:40656,6c25f7075eddb697cb55a53a73e2f686d58b3f76@161.97.128.243:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:55656,d9201d865b1ce2709b0a5270a230d534e93ada2d@65.109.65.163:22056,de11c79dab6ea248fb72f9d93c2ff0eace14a5ac@94.250.201.130:26656,613552eb3c5eba763aeeee8de3d35a3d320a0d23@95.217.56.91:18656,9ba72280b70917ae61300dbb6d1ae8f9bb849172@75.119.159.120:26656,37f1c41be15a41e33a0a820d55db3ca439486602@148.251.90.138:18656,3afe6df94dc385efa85aef823e038c76147e4c99@95.217.35.111:26656,624b1a13e77bd9f3cde44f4ed6a32eff1a95611b@195.201.59.194:26156,173262935b9d8ac15013c3e34936c89de9973f2d@41.189.187.235:26656,15771784ec6a7178d7edf46a3e6f15434f3cdb17@75.119.154.96:26656,e34cc8a12a5274272ff861b4fe3042e98697e500@46.17.250.108:60956,a9986cb9e9950320e3b378a5dadebd6465d09de0@65.21.205.241:18656,02f078c98af4734840834d461bb8d4cbf1a1d68b@95.217.35.112:18656,6452c82f6e479b764a23a5886855cdd67ba0d01b@84.46.247.94:26656,f88ec43f46bf2e20e9ef8560c9e3e484d78fa6b5@194.163.187.112:26656,2fb0a8dd1c16b363d779229ab009479e0e60b7c1@95.129.57.179:36656,2d664a21e72e75f8f5997b1dae9432a0aa8003be@176.101.104.2:26656,244cb3a0c72cfd0a6abd138fb9a3982ff85aeaf3@217.76.49.183:26656,cf08358a4db35d91b0b857e674380828619fcd4c@194.233.81.122:26656,b7931fd033272aadea46c13b8f4aee91309e8c81@65.109.48.181:27656,3dba68e8593170a998fc336951e3a2535c2fd54c@135.181.163.178:18656,2226b7ea3b32ef5cb0bae1162c2bd9d61da03236@87.117.38.192:26656,8ec57a5df11286f36908cce951edb730ce188ea2@86.48.1.140:55656,040d0b6ffefba3283b5763e26c352c7b1b232c1f@65.109.90.171:34656,e0c9d395fcddd5f823dcb179c5c99c1bfbc1b11f@104.193.255.33:26656,eb3a413b8a2baf1f544d4129572919257d5db53b@65.109.82.112:28656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.cascadiad/config/config.toml
```
