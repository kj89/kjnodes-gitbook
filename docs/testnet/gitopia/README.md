# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gitopia.png" width="150" alt=""><figcaption></figcaption></figure>

Gitopia is the next-generation Code Collaboration Platform fuelled by  a decentralized network and interactive token economy. It is designed  to optimize the open-source software development process through  collaboration, transparency, and incentivization.

**Chain ID**: gitopia-janus-testnet-2 | **Latest Version Tag**: v1.2.0 | **Wasm**: OFF

[Website](https://gitopia.com/) | [Discord](https://discord.gg/hFTXCGNYDZ) | [Twitter](https://twitter.com/gitopiaDAO)


## Public endpoints

* rpc: [https://gitopia-testnet.rpc.kjnodes.com](https://gitopia-testnet.rpc.kjnodes.com)
* api: [https://gitopia-testnet.api.kjnodes.com](https://gitopia-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@gitopia-testnet.rpc.kjnodes.com:41656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@gitopia-testnet.rpc.kjnodes.com:41659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/gitopia-testnet/addrbook.json > $HOME/.gitopia/config/addrbook.json
```

**live-peers** (35)
```
peers="9cd6d2477d278ef6ccffa5cc4e22fd0d9489cd23@85.10.199.157:34656,c19da021d6bbdeccdd03453a021d7171e6e299d5@173.249.14.30:656,ea53a3f77fe373f47be4e77fd5f9ff526dfaec33@51.79.143.46:41656,78bacb195b64de732dda6bb2e2839e677c37147a@65.109.90.62:41656,02c20307295465ab2592fd81176e66be90d4bbe2@5.189.159.111:26656,8e9c65f65157cd5540e94335ae068c4040cf9b3b@83.171.249.165:656,5171aad5f862d474b36fc8049be3339068c96cc9@165.232.151.144:26656,f06f794dcc5964197da0e13709d71ea5e0f5b7f1@88.99.3.158:11156,ad33cf22f96e43448798686ed0f7428b8fdacf5b@5.161.90.174:656,ee812a11525cf7e2de4bd63e66aed8b8de337902@38.242.235.199:41656,7f2339fc6a6dca666d8ffbbe4e61443d58e0e759@109.123.255.8:26656,e9e671e22d794a4f80e32133905c83585b057a5d@86.48.3.0:26656,5fb72a0bea398ce56fa20cd732623f98d774be7d@149.102.128.208:41656,5b599e2470b01f8afa88448899f436130fb2e2fd@146.190.112.167:26656,4ceba74efb843cf10926a9ec757e4e2081d71e92@207.244.226.183:656,38f4e436b28b05850fa9b67cadf0700123cec094@45.10.154.166:26656,fea7c372588898f7ea3a04373c52a30712b3c279@185.239.209.56:656,407eb21b784f1dc4e9902cb812b65eec760c6a19@185.193.66.67:656,eccdf1d5bf33bc1733838562b4d4a4a45869c3a8@135.181.183.93:41656,c820e754c56b5455d64ab7685730c44a936d0833@154.38.165.129:26656,2e714e8854361967515a8b859f8f4b0d9b8d11e8@194.163.190.86:26656,8c1c2c5430b9603eae97cbfe5c55a3601ece2aa6@143.198.140.46:26656,730983044bcc3f8e688bc2436da8a171fd843922@154.12.243.189:656,3bcba60fe08bb6ce59abc19b84cf58e7c915e0ed@193.46.243.243:656,ccf24b1e4f8566f3914c08e13d2b6154ed47ddbd@45.153.48.45:26656,aba9c58344ec5e7dcd5ea1dc273d853e58b2ddd9@37.187.78.201:41656,374da78901e59810277fc35482bce6e30953f488@80.79.6.155:41656,afbed8b52881b2f783df0cb07865a4da2fbbdf5e@167.235.243.27:26656,5f045d143cdf9ac78821e848cb10f9c861f5e272@89.117.56.126:24256,5c74fe6868cda2003926c0a6299c9cebec5c4d1a@65.21.239.60:41656,165c6969e40fa2ae2340d8e9fa79a14589a46406@185.193.66.202:26656,5ffdc1788f68df5e8163d9bd0d71a4c4d3dec2e9@81.0.220.21:26656,912035703a495b7491e6300ee6155ea442346340@45.151.122.189:656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,8bec864d68a2542233ba37ac94c723fdf0b8e175@45.151.122.136:656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
