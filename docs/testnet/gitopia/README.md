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
peers="b44d4fd0799d2c06fbec0257b376c0520bdb226a@185.250.37.147:41656,d15e22d7be8ba1b97ff429cf87fea2af41450b37@149.102.134.212:41656,f4d2fd4a8f21c40559b1c903aaae0b0b1c937dc4@194.61.28.39:41656,ad33cf22f96e43448798686ed0f7428b8fdacf5b@5.161.90.174:656,d7f23c752c5790b9647e961277a4767f1ba33f20@95.216.168.99:36656,98bdfc67810bf7ac8f5c45b2c677b4bf199eb42e@185.193.67.65:41656,ee812a11525cf7e2de4bd63e66aed8b8de337902@38.242.235.199:41656,fccf79904b3c03488955d580509d0cc65bb3bb56@65.21.104.192:26656,c19da021d6bbdeccdd03453a021d7171e6e299d5@173.249.14.30:656,e79532749fb5dd95366f4568a7b2430d0e316fb5@84.46.255.163:26656,91bf3eb973595dd4621ccf5853e5ac78c48058da@194.163.180.77:656,458a98d6293064bdf3d6f86e0e2aa87bbb450f07@75.119.144.48:656,c820e754c56b5455d64ab7685730c44a936d0833@154.38.165.129:26656,5ffdc1788f68df5e8163d9bd0d71a4c4d3dec2e9@81.0.220.21:26656,95fbdc6d62be17db6688222b15b57d3e795ed07a@167.86.84.102:656,66f94651fb02f277c90c605a38df549d3c0a9269@75.119.151.217:26656,995177c4b8c2b498de50483a614f9e30bf02e843@65.109.130.180:26656,8f4c2887e46edc200a95afeaa87cb63bdddd26e2@185.239.208.131:656,2ef464f5acb300ed319f18fb082c7455a05e7cca@89.163.209.88:26656,32245abf64927891bb1b6726c24a984d687ebbaf@38.242.153.36:41656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:41656,2e714e8854361967515a8b859f8f4b0d9b8d11e8@194.163.190.86:26656,ebeba690d8084592a983da1e6429598cc9b9d04c@213.202.212.77:26656,3989c44e8af3427b22a71a94185e85df99d450b4@149.102.158.188:41656,5c2c2b27e1824097d4f5dc7a581a8d615923e76f@185.252.235.110:41656,ea53a3f77fe373f47be4e77fd5f9ff526dfaec33@51.79.143.46:41656,38f4e436b28b05850fa9b67cadf0700123cec094@45.10.154.166:26656,374da78901e59810277fc35482bce6e30953f488@80.79.6.155:41656,8e9c65f65157cd5540e94335ae068c4040cf9b3b@83.171.249.165:656,4ceba74efb843cf10926a9ec757e4e2081d71e92@207.244.226.183:656,016b0e565abd496b9473b87ac41339251005d12e@194.163.167.163:41656,f552c1503a04d2455bec87d1d427884e5282bae1@176.9.22.117:41656,c40217eafa32447028bfe62f3c4dd20c14cef94e@173.249.57.208:656,b6651c7b043ef4bdccd7906b0f06de2bbdfe8a60@193.46.243.75:26656,05fa81c618612d6730cb8b54620954ce384899af@146.190.218.191:41656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gitopia/config/config.toml
```
